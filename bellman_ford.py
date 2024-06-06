class BellmanFord:
    def __init__(self, edges, vertexes, int_to_letter_dict):
        self.edges = edges
        self.vertexes = vertexes
        self.int_to_letter_dict = int_to_letter_dict
        self.distances = []
        self.parents = []
        self.negative_cycle_nodes = set()

    def initialize_single_source_vertex(self, start):
        self.distances = [float('inf')] * len(self.vertexes)
        self.parents = [-1] * len(self.vertexes)
        self.distances[start - 1] = 0

    def relax(self, origin, destiny, weight):
        if self.distances[destiny - 1] > self.distances[origin - 1] + weight:
            self.distances[destiny - 1] = self.distances[origin - 1] + weight
            self.parents[destiny - 1] = origin

    def bellman_ford(self, start):
        self.initialize_single_source_vertex(start)
        num_vertices = len(self.vertexes)

        for _ in range(num_vertices - 1):
            for (u, v, w) in self.edges:
                self.relax(u, v, w)

        for (u, v, w) in self.edges:
            if self.distances[v - 1] > self.distances[u - 1] + w:
                self.mark_negative_cycle(v)

    def mark_negative_cycle(self, node):
        if node not in self.negative_cycle_nodes:
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in self.negative_cycle_nodes:
                    self.negative_cycle_nodes.add(current)
                    for (u, v, w) in self.edges:
                        if u == current and v not in self.negative_cycle_nodes:
                            stack.append(v)

    def get_path(self, start, end):
        path = []
        current = end
        while current != -1 and current != start:
            path.append(current)
            current = self.parents[current - 1]
        if current == start:
            path.append(start)
        path.reverse()
        return path

    def int_to_letter(self, num):
        return self.int_to_letter_dict.get(num, "Invalid number")

    def print_paths(self, start):
        for vertex in self.vertexes:
            if vertex in self.negative_cycle_nodes:
                print(f"Vertex {self.int_to_letter(vertex)} cannot be accessed due to a negative cycle")
            elif vertex != start:
                path = self.get_path(start, vertex)
                if self.distances[vertex - 1] == float('inf'):
                    print(f"Path from {self.int_to_letter(start)} to {self.int_to_letter(vertex)}: No path")
                else:
                    new_path = []
                    for i in path:
                        new_path.append(self.int_to_letter(i))
                    print(f"Path from {self.int_to_letter(start)} to {self.int_to_letter(vertex)}: {' -> '.join(map(str, new_path))} with total weight {self.distances[vertex - 1]}")
