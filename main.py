from weight_matrix import WeightMatrix


def read_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            data.append(parts)
    return data


def create_vertexes(number):
    vertexes = []
    for i in range(number):
        vertexes.append(i + 1)
    return vertexes


if __name__ == '__main__':
    graph_input = read_data("input.txt")
    num_vertexes = int(graph_input[0][0])
    vertexes = create_vertexes(num_vertexes)

    edges = []
    edges_weight = []

    for edge_info in graph_input[1:]:
        edge = [int(edge_info[0]), int(edge_info[1])]
        weight = int(edge_info[2])
        edges.append(edge)
        edges_weight.append(weight)

    graph = WeightMatrix(vertexes, edges, edges_weight).graph

    for row in graph:
        print(' '.join(map(str, row)))
