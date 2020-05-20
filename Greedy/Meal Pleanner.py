import sys, operator, random,io, os, types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
from nutrition import Food, MealPlan
'''
def find_notebook(fullname, path=None):
    """find a notebook, given its fully qualified name and an optional path

    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.
    """
    name = fullname.rsplit('.', 1)[-1]
    if not path:
        path = ['']
    for d in path:
        nb_path = os.path.join(d, name + ".ipynb")
        if os.path.isfile(nb_path):
            return nb_path
        # let import Notebook_Name find "Notebook Name.ipynb"
        nb_path = nb_path.replace("_", " ")
        if os.path.isfile(nb_path):
            return nb_path
class NotebookLoader(object):
    """Module Loader for Jupyter Notebooks"""
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path

    def load_module(self, fullname):
        """import a notebook as a module"""
        path = find_notebook(fullname, self.path)

        print ("importing Jupyter notebook from %s" % path)

        # load the notebook object
        with io.open(path, 'r', encoding='utf-8') as f:
            nb = read(f, 4)


        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(fullname)
        mod.__file__ = path
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[fullname] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__

        try:
          for cell in nb.cells:
            if cell.cell_type == 'code':
                # transform the input to executable Python
                code = self.shell.input_transformer_manager.transform_cell(cell.source)
                # run the code in themodule
                exec(code, mod.__dict__)
        finally:
            self.shell.user_ns = save_user_ns
        return mod
class NotebookFinder(object):
    """Module finder that locates Jupyter Notebooks"""
    def __init__(self):
        self.loaders = {}

    def find_module(self, fullname, path=None):
        nb_path = find_notebook(fullname, path)
        if not nb_path:
            return

        key = path
        if path:
            # lists aren't hashable
            key = os.path.sep.join(path)

        if key not in self.loaders:
            self.loaders[key] = NotebookLoader(path)
        return self.loaders[key]
sys.meta_path.append(NotebookFinder())
'''
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2500


def load_nutrient_data(file):
    file = open(file, "r")
    food_list = []
    for line in file:
        first_step = line.split(": ")
        second_step = first_step[1].split(", ")
        food = Food(first_step[0], float(second_step[-4]), float(second_step[-2]), float(second_step[-3]), float(second_step[-1]))
        food_list.append(food)
    return food_list


def sort_food_list_by_ratio(list_to_sort, nutrient, reverse):
    def value_to_weight(food):
        nut_quantity = getattr(food, "%s" % nutrient)
        if food.calories != 0:
            return nut_quantity / food.calories
        else:
            return 0
    list_to_sort.sort(key=value_to_weight, reverse=reverse)
    pass


def create_meal_plan(file_ready, nutrient_select, goal_select):

    planner = MealPlan()

    remaining_goal = float(MAX_CALORIES * int(goal_select)) / 100
    sort_food_list_by_ratio(file_ready, nutrient_select, True)
    for food in file_ready:
        food_nutrient_calories = getattr(food, "%s_calories" % nutrient_select)
        if planner.total_calories < MAX_CALORIES and food.calories > 0:
            if food_nutrient_calories/food.calories >= 0.001:
                if food_nutrient_calories <= remaining_goal and food.calories <= MAX_CALORIES - planner.total_calories:
                    planner.add_food(food)
                    remaining_goal -= food_nutrient_calories
                elif remaining_goal > 0:
                    fraction = remaining_goal / food_nutrient_calories
                    food.set_fraction(fraction)
                    if fraction >= 0.05 and food.calories <= MAX_CALORIES - planner.total_calories:
                        planner.add_food(food)
                        remaining_goal -= getattr(food, "%s_calories" % nutrient_select)

    remaining_calories = MAX_CALORIES - planner.total_calories
    print(planner.total_calories)
    print(planner.total_carbs_calories)
    print(remaining_calories)
    sort_food_list_by_ratio(file_ready, nutrient_select, False)
    for food in file_ready:
        if remaining_calories > 0 and food.calories >= 0.1:
            if food.calories <= remaining_calories:
                planner.add_food(food)
                remaining_calories -= food.calories
            elif remaining_calories > 0:
                fraction = remaining_calories/food.calories
                if fraction >= 0.05:
                    food.set_fraction(fraction)
                    planner.add_food(food)
                    remaining_calories -= food.calories
                    break

    return planner

def print_menu():
    print(str("Enter name of food data file: "))
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbohydrates")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()

def inputVerify (promptInput, values, initRange, endRange):
    recivedInput = input(promptInput)
    if recivedInput.isnumeric():
        if int(recivedInput) in range(initRange, endRange):
            if int(recivedInput) == 4:
                sys.exit(0)
            else:
                return recivedInput
        else:
            print(str("Invalid choice! Enter an integer from"), values)
            print_menu()
            return inputVerify(promptInput, values, initRange, endRange)

    else:
        print(str("Invalid choice! enter an integer from"),values)
        return inputVerify(promptInput, values, initRange, endRange)

if __name__ == "__main__":
    filename = "food.txt"
    foods = load_nutrient_data(filename)
    print_menu()
    nutrient_input = inputVerify("Enter choice (1-4):", "1-4!", 1, 5)
    goal_input = inputVerify("Enter choice (0-100)", "0-100!", 0, 101)

    if nutrient_input == "1":
        nutrient_input = "protein"
    elif nutrient_input == "2":
        nutrient_input = "carbs"
    elif nutrient_input == "3":
        nutrient_input = "fat"
    plan = create_meal_plan(foods, nutrient_input, int(goal_input))
    print(plan)