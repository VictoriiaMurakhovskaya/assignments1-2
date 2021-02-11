# Slightly updated February 7

import unittest
from digraph import Digraph


class TestDigraph(unittest.TestCase):
    # The assignment says that the values of .vertices() and .edges()
    # should be "lists or something else it's possible to loop over".
    # So convert to list before checking these values.
    def test_empty(self):
        g = Digraph(vertices=[], edges=[])
        self.assertEqual(list(g.vertices()), [])
        self.assertEqual(list(g.edges()), [])

    # Since it shouldn't matter which order things are listed in those
    # ~lists I make sorted lists of them before comparing.
    def test_adds_vertices(self):
        g = Digraph(vertices=[1], edges=[(2, 3), (3, 4)])
        self.assertEqual(sorted(g.vertices()), [1, 2, 3, 4])
        self.assertEqual(sorted(g.edges()), [(2, 3), (3, 4)])

    # Make this test before other tests where the default value is used.
    def test_reuses_default(self):
        g1 = Digraph(edges=[(1, 2)])
        g2 = Digraph(edges=[(3, 4)])
        self.assertEqual(sorted(g2.vertices()), [3, 4])

    def test_default_vertices(self):
        g = Digraph(edges=[(1, 2), (2, 3)])
        self.assertEqual(sorted(g.vertices()), [1, 2, 3])
        self.assertEqual(sorted(g.edges()), [(1, 2), (2, 3)])

    def test_default_edges(self):
        g = Digraph(vertices=[1, 2, 3])
        self.assertEqual(sorted(g.vertices()), [1, 2, 3])
        self.assertEqual(list(g.edges()), [])

    def test_default_empty(self):
        g = Digraph()
        self.assertEqual(list(g.vertices()), [])
        self.assertEqual(list(g.edges()), [])

    # The example given in the assignment.
    def test_triangle(self):
        g = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[4])
        self.assertEqual(sorted(g.vertices()), [1, 2, 3, 4])
        self.assertEqual(sorted(g.edges()), [(1, 2), (1, 3), (2, 3), (3, 3)])

    def test_add_edge(self):
        g = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[4])
        g.add_edge(5, 3)
        self.assertEqual(sorted(g.vertices()), [1, 2, 3, 4, 5])
        self.assertEqual(sorted(g.edges()),
                         [(1, 2), (1, 3), (2, 3), (3, 3), (5, 3)])

    def test_remove_isolated_vertex(self):
        g = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[4])
        g.remove_vertex(4)
        self.assertEqual(sorted(g.vertices()), [1, 2, 3])

    def test_remove_vertex_with_edges(self):
        g = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[4])
        g.add_edge(5, 3)
        g.remove_vertex(2)
        self.assertEqual(sorted(g.vertices()), [1, 3, 4, 5])
        self.assertEqual(sorted(g.edges()), [(1, 3), (3, 3), (5, 3)])

    def test_transitivity(self):
        g = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[4])
        g.add_edge(5, 3)
        self.assertTrue(g.is_transitive())
        g.add_edge(3, 4)
        self.assertFalse(g.is_transitive())
        g.add_edge(5, 4)
        self.assertFalse(g.is_transitive())
        g.add_edge(2, 4)
        self.assertFalse(g.is_transitive())
        g.add_edge(1, 4)
        self.assertTrue(g.is_transitive())


if __name__ == '__main__':
    unittest.main()
