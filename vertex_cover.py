import numpy as np
from collections import defaultdict
import time

class VertexCover:
    def __init__(self, graph_adjacency_matrix : np.ndarray):
        self.adjacency = graph_adjacency_matrix
        try:
            assert np.allclose(self.adjacency, self.adjacency.T)
        except AssertionError:
            print("Adjacency Matrix is not symmetric, please check!")
            raise
        self.num_vertices = len(self.adjacency)
        self.graph = self._get_graph_from_adjacency(self.adjacency)

    def _get_graph_from_adjacency(self, adjacency_matrix) -> dict:
        graph_dict = defaultdict(list)

        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if adjacency_matrix[u][v] == 1:
                    graph_dict[u].append(v)

        return graph_dict

    def get_vertex_cover(self) -> tuple:
        covering_vertices = [False] * self.num_vertices
        start = time.time() * 1e6
        for u in range(self.num_vertices):
            if not covering_vertices[u]:
                for v in self.graph[u]:
                    if not covering_vertices[v]:
                        covering_vertices[v] = True
                        covering_vertices[u] = True
                        break
        end = time.time() * 1e6
        return (covering_vertices.count(True), np.where(covering_vertices)[0], (end - start))