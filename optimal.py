import greedy
import graph
import itertools

class OptimalSolution(greedy.GreedySolution):

    def reset(self):
        """Reset its solution set and vertex distances"""
        self.solution_set = []
        self.dist_to_soln = []

def run_optimal(graph, k = 1):
    """Run the optimal (bruteforce) algorithm and return the solution set and its cost

    Arguments:
    graph: graph is the input graph, either a Graph instance or a 2D array,
           it must be complete and satisfy triangular inequality
    k (int): the k value for k-centre (default 1)
    """
    # Check graph type
    try:
        graph = graph.graph
    except AttributeError:
        pass

    # Find all possible combinations of k sized solution sets
    all_solution_sets = list(itertools.combinations(range(len(graph)), k))
    
    solution = OptimalSolution(graph)
    
    # Check first candidate
    count = 0
    for i in range(len(graph)):
        dist_i_to_soln = (graph[i][j] for j in all_solution_sets[0])
        solution.dist_to_soln.append(min(dist_i_to_soln))
    optimal_cost = solution.cost()
    optimal_solution_set = [x for x in all_solution_sets[0]]
    solution.reset()

    # Check all other candidates, keeping the best candidate and cost
    for candidate in all_solution_sets[1:]:
        for i in range(len(graph)):
            dist_i_to_soln = (graph[i][j] for j in candidate)
            solution.dist_to_soln.append(min(dist_i_to_soln))
        count += 1
        if solution.cost() < optimal_cost:
            optimal_cost = solution.cost()
            optimal_solution_set = [x for x in candidate]
        solution.reset()

    return optimal_solution_set, optimal_cost

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
    
    solution_set, cost = run_optimal(graph,k)

    print "THE SOLUTION SET IS %s" % (solution_set,)
    print "THE COST IS %s" % (cost,)
