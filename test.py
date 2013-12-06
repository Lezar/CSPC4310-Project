import unittest
import graph
import math

class TestGraph(unittest.TestCase):
    """Test whether graph generator creates metric graphs"""

    def setUp(self):
        pass

    def test_distance1(self):
        """Test the distance function of graph"""
        point1 = (0,0)
        point2 = (6,6)
       
        dist12 = int(math.sqrt((6-0)**2 + (6-0)**2))
        self.assertEqual(graph.distance(point1, point2), dist12)

    def test_distance2(self):
        """Test the distance function of graph"""
        point1 = (13,1)
        point2 = (32,123)

        dist12 = int(math.sqrt((32-13)**2 + (123-1)**2))
        self.assertEqual(graph.distance(point1, point2), dist12)

    def test_generate_graph_size_5(self):
        """Test if Graph can construct a graph of size 5"""
        graph5 = graph.Graph(5)
        self.assertEqual(len(graph5.graph), 5)
        self.assertEqual(len(graph5.graph[0]), 5)
        self.assertEqual(len(graph5.graph[1]), 5)
        self.assertEqual(len(graph5.graph[2]), 5)
        self.assertEqual(len(graph5.graph[3]), 5)
        self.assertEqual(len(graph5.graph[4]), 5)

    def test_generate_graph_size_9(self):
        """Test if Graph can construct a graph of size 9"""
        graph9 = graph.Graph(9)
        self.assertEqual(len(graph9.graph), 9)
        self.assertEqual(len(graph9.graph[0]), 9)
        self.assertEqual(len(graph9.graph[1]), 9)
        self.assertEqual(len(graph9.graph[2]), 9)
        self.assertEqual(len(graph9.graph[3]), 9)
        self.assertEqual(len(graph9.graph[4]), 9)
        self.assertEqual(len(graph9.graph[5]), 9)
        self.assertEqual(len(graph9.graph[6]), 9)
        self.assertEqual(len(graph9.graph[7]), 9)
        self.assertEqual(len(graph9.graph[8]), 9)

    def test_generate_graph_size_4_is_metric(self):
        """Test if Graph can construct a metric graph of size 4"""
        metric_graph_4 = graph.Graph(4)
        self.assertEqual(len(metric_graph_4.graph), 4)
        
        #Test triangle inequality
        for u in range(len(metric_graph_4.graph)):
            for v in range(len(metric_graph_4.graph)):
                for w in range(len(metric_graph_4.graph)):
                    dist_uv = metric_graph_4.graph[u][v]
                    dist_vw = metric_graph_4.graph[v][w]
                    dist_wu = metric_graph_4.graph[w][u]

if __name__ == '__main__':
    unittest.main()
