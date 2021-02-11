import numpy as np


class Digraph:
    def __init__(self, edges=None, vertices=None):
        if vertices is None:
            vertices = []
        if edges is None:
            edges = []
        self.setedges = set()
        self.setvertices = set()

        for source, dest in edges:
            self.setedges.add((source, dest))
            self.setvertices.add(source)
            self.setvertices.add(dest)
        for vertex in vertices:
            self.setvertices.add(vertex)

    def edges(self):
        return list(self.setedges)

    def vertices(self):
        return list(self.setvertices)

    def addvertex(self, vertex):
        self.setvertices.add(vertex)

    def add_edge(self, source, dest):
        self.setedges.add((source, dest))
        self.setvertices.add(source)
        self.setvertices.add(dest)

    def remove_vertex(self, vertex):
        self.setvertices.remove(vertex)

        edged_to_remove = []
        for source, dest in self.setedges:
            if source == vertex or dest == vertex:
                edged_to_remove.append((source, dest))
        for item in edged_to_remove:
            self.setedges.remove(item)

    def adj_matrix(self):
        m = np.zeros((len(self.vertices()), len(self.vertices())))
        for edge in self.setedges:
            m[edge[0] - 1, edge[1] - 1] = 1
        return m

    def is_transitive(self):
        """
        uses Warshall algorithm
        :return:
        """
        R = self.adj_matrix()
        n = len(R)
        S = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (R[j, k] == 1) & (R[i, j] == 1):
                        if R[i, k] != 1:
                            return False
        return True

