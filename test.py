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
        
        # Test triangle inequality
        for u in range(len(metric_graph_4.graph)):
            for v in range(u, len(metric_graph_4.graph)):
                for w in range(v, len(metric_graph_4.graph)):
                    dist_uv = metric_graph_4.graph[u][v]
                    dist_vw = metric_graph_4.graph[v][w]
                    dist_wu = metric_graph_4.graph[w][u]
                    self.assertTrue(dist_uv <= dist_vw + dist_wu)
                    self.assertTrue(dist_vw <= dist_wu + dist_uv)
                    self.assertTrue(dist_wu <= dist_uv + dist_vw)

    def test_graph_is_symmetric(self):
        """Test if graphs constructed are symmetric"""
        graph_10 = graph.Graph(11)
        
        # Test symmetry
        for u in range(len(graph_10.graph)):
            for v in range(len(graph_10.graph)):
                self.assertEqual(graph_10.graph[u][v], graph_10.graph[v][u])

    def test_graph_generate_1_point(self):
        """Test if Graph can generate 1 points"""
        graph_1 = graph.Graph(1)
        graph_1.generate_graph(1)
        self.assertEqual(len(graph_1.points), 1)

    def test_graph_generate_11_points(self):
        """Test if Graph can generate 11 points"""
        graph_11 = graph.Graph(11)
        graph_11.generate_graph(11)
        self.assertEqual(len(graph_11.points), 11)

    def test_graph_points_are_not_all_same(self):
        """Test that points generated are not all the same (or else problem is trivial)"""
        graph_20 = graph.Graph(20)
        graph_20.generate_graph(20)

        same = True        

        for u in range(len(graph_20.points)):
            for v in range(u, len(graph_20.points)):
                if graph_20.points[u] != graph_20.points[v]:
                    same = False

        self.assertFalse(same)

    def test_graph_is_distances_of_points(self):
        """Test that the graph is a complete graph were edge weights are distances of points"""
        graph_23 = graph.Graph(23)
        graph_23.generate_graph(23)

        # Check distances for every point in points and graph
        for u in range(len(graph_23.graph)):
            for v in range(len(graph_23.graph)):
                graph_dist_uv = graph_23.graph[u][v]
                point_dist_uv = graph.distance(graph_23.points[u], graph_23.points[v])
                self.assertEqual(graph_dist_uv, point_dist_uv)

    def test_generate_graph_size_10_is_metric(self):
        """Test if Graph can construct a metric graph of size 10"""
        metric_graph_10 = graph.Graph(10)
        self.assertEqual(len(metric_graph_10.graph), 10)
        
        # Test triangle inequality
        print metric_graph_10. points
        for u in range(len(metric_graph_10.graph)):
            for v in range(u, len(metric_graph_10.graph)):
                for w in range(v, len(metric_graph_10.graph)):
                    dist_uv = metric_graph_10.graph[u][v]
                    dist_vw = metric_graph_10.graph[v][w]
                    dist_wu = metric_graph_10.graph[w][u]
                    self.assertTrue(dist_uv <= dist_vw + dist_wu)
                    self.assertTrue(dist_vw <= dist_wu + dist_uv)
                    self.assertTrue(dist_wu <= dist_uv + dist_vw)

    def test_write_graph(self):
        """Test if Graph can save to CSV file"""
        graph_10 = graph.Graph(10)
        graph_10.write_to_csv("test_write_graph.csv")
        loaded_graph_10 = graph.Graph()
        loaded_graph_10.read_from_csv("test_write_graph.csv")

        # First check that size is correct
        self.assertEqual(len(loaded_graph_10.graph), 10)
        self.assertEqual(len(loaded_graph_10.graph), 10)
        self.assertEqual(len(loaded_graph_10.graph[0]), 10)
        self.assertEqual(len(loaded_graph_10.graph[1]), 10)
        self.assertEqual(len(loaded_graph_10.graph[2]), 10)
        self.assertEqual(len(loaded_graph_10.graph[3]), 10)
        self.assertEqual(len(loaded_graph_10.graph[4]), 10)
        self.assertEqual(len(loaded_graph_10.graph[5]), 10)
        self.assertEqual(len(loaded_graph_10.graph[6]), 10)
        self.assertEqual(len(loaded_graph_10.graph[7]), 10)
        self.assertEqual(len(loaded_graph_10.graph[8]), 10)
        self.assertEqual(len(loaded_graph_10.graph[9]), 10)

        # Check that each element is equal
        for u in range(len(graph_10.graph)):
            for v in range(u, len(graph_10.graph)):
                self.assertEqual(loaded_graph_10.graph[u][v], graph_10.graph[u][v])
                self.assertEqual(loaded_graph_10.graph[v][u], graph_10.graph[v][u])

if __name__ == '__main__':
    unittest.main()
