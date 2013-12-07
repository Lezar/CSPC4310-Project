import unittest
import graph
import math
import greedy

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

    def test_generate_graph_size_30_is_metric(self):
        """Test if Graph can construct a metric graph of size 20"""
        metric_graph_30 = graph.Graph(30)
        self.assertEqual(len(metric_graph_30.graph), 30)
        
        # Test triangle inequality
        for u in range(len(metric_graph_30.graph)):
            for v in range(u, len(metric_graph_30.graph)):
                for w in range(v, len(metric_graph_30.graph)):
                    dist_uv = metric_graph_30.graph[u][v]
                    dist_vw = metric_graph_30.graph[v][w]
                    dist_wu = metric_graph_30.graph[w][u]
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

class TestGreedy(unittest.TestCase):
    """Tests the greedy k-centre"""

    def setUp(self):
        self.graph10 = graph.Graph(10)
        self.graph10.graph =[[0,22,40,48,7,85,59,51,75,31],
                            [22,0,18,62,24,64,50,41,53,48],
                            [40,18,0,73,41,46,44,35,35,62],
                            [48,62,73,0,41,103,56,55,100,17],
                            [7,24,41,41,0,83,53,46,75,25],
                            [85,64,46,103,83,0,50,48,14,98],
                            [59,50,44,56,53,50,0,9,51,56],
                            [51,41,35,55,46,48,9,0,47,52],
                            [75,53,35,100,75,14,51,47,0,92],
                            [31,48,62,17,25,98,56,52,92,0]]

        self.solution = greedy.GreedySolution(self.graph10)

    def test_solution_adds_vertex(self):
        """Tests if the GreedySolution can add a vertex to its solution set"""  

        # Add index 1 and test size and in solution
        self.solution.add_vertex(1)
        self.assertTrue(1 in self.solution.solution_set)
        self.assertEqual(len(self.solution.solution_set), 1)

        # Add index 5 and test size and in solution
        self.solution.add_vertex(5)
        self.assertTrue(1 in self.solution.solution_set)
        self.assertTrue(5 in self.solution.solution_set)
        self.assertEqual(len(self.solution.solution_set), 2)

    def test_distance_from_vertex_to_solution(self):
        """Tests if the distance from a vertex to solution set is properly calculated"""
        self.solution.add_vertex(6)
        self.solution.add_vertex(7)
        self.solution.add_vertex(8)
        self.solution.add_vertex(9)
        self.assertTrue(self.solution.dist_to_soln[5], 14)
        self.assertTrue(self.solution.dist_to_soln[3], 25)

    def test_find_farthest_vertex(self):
        """Tests if greedy can find the farthest vertex to add to its solution"""
        # Test first by adding 3
        self.solution.add_vertex(3)
        next_vertex = self.solution.find_farthest_vertex()
        self.assertEquals(next_vertex, 5)
        
        # Test by adding 5
        self.solution.add_vertex(5)
        next_vertex = self.solution.find_farthest_vertex()
        self.assertEquals(next_vertex, 1)

    def test_determine_cost_of_solution_set(self):
        self.solution.add_vertex(3)
        self.solution.add_vertex(6)
        self.solution.add_vertex(7)
        self.assertEquals(self.solution.cost(), 277)

    def test_find_greedy_solution_set_k4(self):
        """Find the greedy solution set for graph10 when k = 4 given starting vertex 1"""
        solution_set, cost = greedy.run_greedy(self.graph10, k = 4, start_vertex = 1)
        self.assertTrue(1 in solution_set)
        self.assertTrue(5 in solution_set)
        self.assertTrue(3 in solution_set)
        self.assertTrue(6 in solution_set)
        self.assertEquals(cost, 104)

    def test_find_greedy_solution_set_k3(self):
        """Find the greedy solution set for K_9 when k = 3 given starting vertex 7"""
        graph9 = [[0,651,168,449,540,199,209,310,247],
                [651,0,581,542,322,629,493,387,424],
                [168,581,0,539,559,60,275,332,266],
                [449,542,539,0,238,597,264,247,290],
                [540,322,559,238,0,619,331,233,300],
                [199,629,60,597,619,0,333,392,326],
                [209,493,275,264,331,333,0,111,72],
                [310,387,332,247,233,392,111,0,67],
                [247,424,266,290,300,326,72,67,0]]
        solution_set, cost = greedy.run_greedy(graph9, k = 3, start_vertex = 7)
        self.assertTrue(7 in solution_set)
        self.assertTrue(1 in solution_set)
        self.assertTrue(5 in solution_set) 
        self.assertEquals(cost, 917)

if __name__ == '__main__':
    unittest.main()
