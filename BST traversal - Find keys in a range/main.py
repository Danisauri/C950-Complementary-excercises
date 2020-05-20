from BinarySearchTree import BinarySearchTree, Node

array_of_keys = []
def find_in_range(current_node, beginning_range, ending_range):
    begin = ascii(beginning_range)
    end = ascii(ending_range)
    while current_node is not None:
        if current_node.key > end and current_node.left is not None:
            current_node = current_node.left
        elif current_node.key < begin and current_node.right is not None:
            current_node = current_node.right
        else: #estamos en el rango
            if current_node.left is not None:
                current_node = current_node.left
            elif current_node.right is not None:
                if current_node.key not in array_of_keys:
                    array_of_keys.append(current_node.key)
                    tree.remove(current_node.key)
                current_node = current_node.right
            elif current_node.key not in array_of_keys:
                array_of_keys.append(current_node.key)
                tree.remove(current_node.key)
                find_in_range(root_node, beginning_range, ending_range)
            else:
                # final_array = []
                # for i in array_of_keys:
                #     if ascii(i) <= end and ascii(i) >= begin:
                #         final_array.append(i)
                return array_of_keys


# Main
if __name__ == "__main__":
    tree = BinarySearchTree()
    keys_in_range = []

    # Insert some random-looking integers into the tree.
    user_values = "bat start ding being clock quick last name truck"#input('Enter values to be inserted separated by spaces: ')
    print()

    for value in user_values.split():
        new_node = Node(value)
        tree.insert(new_node)

    print('Initial tree:')
    print(tree)
    print()

    # Read in range values and starting node's key
    beginning_range = "craft"#input("beginning")
    ending_range = "question"#input("ending")
    starting_node = "ding"#input("start")

    # Find starting node in tree
    root_node = Node(tree.search(starting_node)).key


    # Find keys in range from starting node
    keys_in_range = find_in_range(root_node, beginning_range, ending_range)

    # Output list of keys in range
    print('Keys in range:', keys_in_range)