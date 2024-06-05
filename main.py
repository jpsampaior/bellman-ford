from bellman_ford import BellmanFord


# Função para ler os dados do arquivo
def read_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            data.append(parts)
    return data


# Função para criar a lista de vértices
def create_vertexes(number):
    vertexes = []
    for i in range(number):
        vertexes.append(i + 1)
    return vertexes


if __name__ == '__main__':
    graph_input = read_data("input2.txt")
    num_vertexes = int(graph_input[0][0])
    vertexes = create_vertexes(num_vertexes)

    edges = []

    for edge_info in graph_input[1:]:
        origin = int(edge_info[0])
        destiny = int(edge_info[1])
        weight = int(edge_info[2])
        edges.append((origin, destiny, weight))

    bf = BellmanFord(edges, vertexes)
    start_vertex = 1
    result = bf.bellman_ford(start_vertex)

    bf.print_paths(start_vertex)