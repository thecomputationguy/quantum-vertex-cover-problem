import numpy as np
from collections import defaultdict
import time

class VertexCover:
    """Class to determine the vertex cover from the adjacency matrix of a graph.
    """    
    def __init__(self, graph_adjacency_matrix : np.ndarray):
        """Generate a dictionary of nodes and their edges from an adjacency matrix.

        Parameters
        ----------
        graph_adjacency_matrix : np.ndarray
            Adjacency matrix of the grpah.
        """        
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
        """Get the vertex cover using the algorithm from CLRS, Section 35.1

        Returns
        -------
        tuple
            Vertex Cover size, Nodes in the cover, Approximate time-of-run
        """        
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