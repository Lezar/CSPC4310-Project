import graph
import heapq
import random

class GreedySolution():

    def __init__(self, graph):

        # Check graph type
        try:
            graph = graph.graph
        except AttributeError:
            pass

        self.graph = graph
        self.solution_set = []
        self.vertices = [[] for x in range(len(graph))]
        for list in self.vertices:
            heapq.heapify(list)
        

    def add_vertex(self, vertex):
        """Add a vertex to the solution set

        Arguments:
        vertex (int): the index of the vertex to be added
        """
        self.solution_set.append(vertex)
        
        for v in range(len(self.vertices)):
            dist_v_vertex = self.graph[v][vertex]
            heapq.heappush(self.vertices[v], dist_v_vertex)

    def find_farthest_vertex(self):
        """Return the index of the farthest vertex from solution_set"""
        # Create a list of tuples (w,v) where w is the distances of vertex v from solution set
        distances = [(-self.vertices[v][0], v) for v in range(len(self.vertices))]
        heapq.heapify(distances)
        return distances[0][1]

    def cost(self):
        """Return the total cost of the current solution"""
        total_cost = 0
        for v in self.vertices:
            total_cost += v[0]
        return total_cost

def run_greedy(graph, k = 1, start_vertex = None):
    """Run the greedy algorithm and return the solution set and its cost

    Arguments:
    graph: graph is the input graph, either a Graph instance or a 2D array,
           it must be complete and satisfy triangular inequality
    k (int): the k value for k-centre (default 1)
    starting_vertex (int): the index of the starting vertex (default None)
    """
    # Check graph type
    try:
        graph = graph.graph
    except AttributeError:
        pass
    
    # Random starting vertex if none is selected
    if start_vertex is None:
        random.seed()
        start_vertex = int(random.random() * len(graph))

    solution = GreedySolution(graph)

    # Rune greedy until there are k centres chosen
    solution.add_vertex(start_vertex)
    next_vertex = solution.find_farthest_vertex()
    while len(solution.solution_set) < k:
        solution.add_vertex(next_vertex)
        next_vertex = solution.find_farthest_vertex()

    return solution.solution_set, solution.cost()
        
