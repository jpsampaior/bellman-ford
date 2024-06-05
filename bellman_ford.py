class BellmanFord:
    def __init__(self, edges, vertexes):
        self.edges = edges
        self.vertexes = vertexes
        self.distances = []
        self.parents = []

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
                print(f"Negative cycle detected via edge ({v}, {u})")
                return False

        return True

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

    def print_paths(self, start):
        for vertex in self.vertexes:
            if vertex != start:
                path = self.get_path(start, vertex)
                if self.distances[vertex - 1] == float('inf'):
                    print(f"Path from {start} to {vertex}: No path")
                else:
                    print(f"Path from {start} to {vertex}: {' -> '.join(map(str, path))} with total weight {self.distances[vertex - 1]}")
