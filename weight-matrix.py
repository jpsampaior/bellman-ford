class WeightMatrix:
    def __init__(self, vertexes, edges, edges_weight):
        self.vertexes = vertexes
        self.edges = edges
        self.edges_weight = edges_weight
        self.num_vertexes = len(vertexes)
        self.eulerian_path = []

        self.graph = [[0] * self.num_vertexes for _ in range(self.num_vertexes)]
        self.add_edge()

        self.vertexDegree_array = []

    def add_edge(self):
        for edge, weight in zip(self.edges, self.edges_weight):
            self.graph[edge[0] - 1][edge[1] - 1] = weight

    def calculate_vertex_degree(self):
        self.vertexDegree_array = []

        for line in self.graph:
            self.vertexDegree_array.append(sum(1 for weight in line if weight > 0))
