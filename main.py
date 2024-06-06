from bellman_ford import BellmanFord
from consts import Consts

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


# Função que retorna o número correspondente de uma letra
def letter_to_int(letra, letter_to_int_dict):
    return letter_to_int_dict.get(letra.upper(), "Invalid letter")


if __name__ == '__main__':
    input_num = input("Selecione qual input você quer (1 ou 2)")
    if input_num.strip() == '1':
        graph_input = read_data("inputOriginal.txt")
        letter_to_int_dict = Consts.letter_to_int_dict_case1
        int_to_letter_dict = Consts.int_to_letter_dict_case1

    elif input_num.strip() == '2':
        graph_input = read_data("input2Original.txt")
        letter_to_int_dict = Consts.letter_to_int_dict_case2
        int_to_letter_dict = Consts.int_to_letter_dict_case2

    num_vertexes = int(graph_input[0][0])
    vertexes = create_vertexes(num_vertexes)

    transformed_list = []

    for sublist in graph_input[1:]:
        transformed_sublist = []
        for item in sublist:
            if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                transformed_sublist.append(int(item))
            else:
                transformed_sublist.append(letter_to_int(item, letter_to_int_dict))
        transformed_list.append(transformed_sublist)

    # Mostrar a lista transformada


    edges = []

    for edge_info in transformed_list:
        origin = int(edge_info[0])
        destiny = int(edge_info[1])
        weight = int(edge_info[2])
        edges.append((origin, destiny, weight))

    bf = BellmanFord(edges, vertexes, int_to_letter_dict)
    start_vertex = input("Defina o vertice de partida")
    start_vertex = letter_to_int(start_vertex.strip(), letter_to_int_dict)

    result = bf.bellman_ford(start_vertex)

    bf.print_paths(start_vertex)