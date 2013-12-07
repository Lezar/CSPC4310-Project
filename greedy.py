import graph
import heapq
import random

class GreedySolution():
    """Generate complete metric graph as a 2D list (matrix) to be used for k-centre

    Constructor Arguments:
    graph: graph is the input graph, either a Graph instance or a 2D array,
           it must be complete and satisfy triangular inequality

    Attributes:
    graph (list): A complete metric graph represented as a 2D list
                  Each entry (i,j) in the array represents the distance between vertices indexed i and j
    solution_set (list): A list of the vertex indices of the current solution
    dist_to_soln (list): A list of the distances from each vertex to the solution_set
    """

    def __init__(self, graph):

        # Check graph type
        try:
            graph = graph.graph
        except AttributeError:
            pass

        self.graph = graph
        self.solution_set = []
        self.dist_to_soln = []

    def add_vertex(self, vertex):
        """Add a vertex to the solution set

        Arguments:
        vertex (int): the index of the vertex to be added
        """
        self.solution_set.append(vertex)
        
        # Calculate distance as the minimum
        if len(self.solution_set) == 1:
            # If it is the first vertex, just add the row list
            self.dist_to_soln = self.graph[vertex]
        else:
            # Otherwise set the distance to the minimum
            for i in range(len(self.dist_to_soln)):
                self.dist_to_soln[i] = min(self.dist_to_soln[i], self.graph[vertex][i])

    def find_farthest_vertex(self):
        """Return the index of the farthest vertex from solution_set"""
        return self.dist_to_soln.index(max(self.dist_to_soln))

    def cost(self):
        """Return the total cost of the current solution"""
        total_cost = 0
        for v in self.dist_to_soln:
            total_cost += v
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

if __name__ == '__main__':
    filename = raw_input('Filename to open: ')
    filename = './data/' + filename + '.csv'

    graph = graph.Graph()
    graph.read_from_csv(filename)

    while(True):
        k = int(raw_input('Please input k: '))
        if k < len(graph.graph):
            break
        print "Graph is size %s. Please adjust your k value." % (len(graph.graph),)
    
    solution_set, cost = run_greedy(graph,k)

    print "THE SOLUTION SET IS %s" % (solution_set,)
    print "THE COST IS %s" % (cost,)
        
