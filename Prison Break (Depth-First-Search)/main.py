import sys
from graph import Graph, Vertex

def create_graph(filename):
    parameters = []
    for line in prison_filename:
        parameters.append(line.rstrip())

    grid_parameters = parameters[0]
    camera_parameters = []

    for camera in range(1,len(parameters)):
        camera_parameters.append(parameters[camera])

    grid_parameters_split = grid_parameters.split()

    final_grid = Graph()

    under_row = []

    for row in reversed(range(int(grid_parameters_split[0]))):
        for column in reversed(range(int(grid_parameters_split[1]))):
            label = str(row)+" "+str(column)
            curr_vertex = Vertex(label)

            if label in camera_parameters:
                curr_vertex.has_camera = True

            final_row = int(grid_parameters_split[0])-1
            final_column = int(grid_parameters_split[1])-1
            if label == str(final_row)+" "+str(final_column):
                exit_vertex = curr_vertex

            final_grid.add_vertex(curr_vertex)
            under_row.append(curr_vertex)

            if column+1 in range(int(grid_parameters_split[1])):
                final_grid.add_undirected_edge(curr_vertex, last_vertex)

            if row+1 in range(int(grid_parameters_split[0])):
                final_grid.add_undirected_edge(curr_vertex, under_row.pop(0))

            last_vertex = curr_vertex

    return final_grid, last_vertex, exit_vertex

count = 0
visited_points = []

def count_exit_paths(g, vertex, exit, visited_points):
    global count
    vertex.visited = True
    visited_points.append(vertex.label)
    if vertex == exit:
        count += 1
        print(visited_points)
    else:
        for adjacent in list(g.adjacency_list.get(vertex)):
            if not adjacent.visited and not adjacent.has_camera:
                count_exit_paths(g, adjacent, exit, visited_points)
    vertex.visited = False
    visited_points.pop()
    return count



prison_filename = open("grid.txt", "r")
# resultados:
# 15x12 = 18186
# 3x4 = 4
# 8x8 = 224


# if __name__ == "__main__":
#     # prison_filename = sys.argv[1]
prison_graph, prisoner_vertex, exit_vertex = create_graph(prison_filename)
num_paths = count_exit_paths(prison_graph, prisoner_vertex, exit_vertex, visited_points)
print(num_paths)
