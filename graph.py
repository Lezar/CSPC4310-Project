import math
import csv
import random

def distance(point1, point2):
    """Find the distance between two points and return it as an integer"""
    return int(math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2))


class Graph():
    """Generate complete metric graph as a 2D list (matrix) to be used for k-centre

    Constructor Arguments:
    n (int): The number of vertices in the graph. Constructor generates 0 matrix of size n x n

    Attributes:
    graph (list): A complete metric graph represented as a 2D list
                  Each entry (i,j) in the array represents the distance between vertices indexed i and j
                  We will ensure the graph is metric by finding distances of points on a plane
    
    """

    def __init__(self, n=1):
        self.graph = [[0]]        
        if n != 1:
            self.generate_graph(n)

    def generate_graph(self, n=1):
        """Generate a complete metric graph

        Generate a complete metric graph by adding points to a plane and using
        the distances between points as edge weights. Because the points are on a plane,
        this ensures triangular inequality.

        Arguments:
        n (int) the size of the graph generated
        """

        self.graph = [0]*n
        for i in range(n):
            self.graph[i] = [0]*n

        random.seed()
        self.points = [(int(random.random()*n*n*n), int(random.random()*n*n*n))]        
        for i in range(1,n):
            print i
            metric = False
            # Ensure triangular inequality as each point is added to the list
            # Generate graph matrix while points are being added
            while not metric:
                metric = True
                
                # Use a large range for random to ensure inequalities occur each time
                # since rounding errors when points are close together may cause the graph
                # to not have the triangular inequality property. This will cause less
                # checks for whether the graph is metric
                point = (int(random.random()*n*n*n), int(random.random()*n*n*n))
                points_size = len(self.points)
                
                # Check if candidate point maintains triangular inequality
                # With the rest of the points already in the graph
                for u in range(points_size):
                    dist_u_point = distance(self.points[u], point)
                    for v in range(u, points_size):
                        
                        dist_point_v = distance(point, self.points[v])
                        dist_vu = distance(self.points[v], self.points[u])

                        if not ((dist_u_point <= dist_point_v + dist_vu) and
                                (dist_point_v <= dist_vu + dist_u_point) and
                                (dist_vu <= dist_u_point + dist_point_v)):
                            metric = False
                    self.graph[u][points_size] = dist_u_point
                    self.graph[points_size][u] = dist_u_point
                            
            self.points.append(point)
    
    def write_to_csv(self, filename):
        """Write to a csv file

        Arguments:
        filename (string): the name of the csv file to write to
        """
        
        # Write to a CSV file row by row
        try:
            with open(filename,'w') as writefile:
                csvwriter = csv.writer(writefile)
                for row in self.graph:
                    csvwriter.writerow(row)
        except IOError, e:
            print "I/O error: %s" % e
        
    def read_from_csv(self, filename):
        """Read from a csv file

        Arguments:
        filename (string): the name of the csv file to read from
        """
        
        self.graph = []

        # Read the file into a string separated by newlines for each row
        try:
            with open(filename,'r') as readfile:
                lines = readfile.read().splitlines()
        except IOError, e:
            print "I/O error: %s" % e
            return

        # Read lines with csv.reader
        csvreader = csv.reader(lines)

        # Load the rows into self.graph matrix
        try:
            for row in csvreader:
                self.graph.append([])
                for element in row:
                    self.graph[csvreader.line_num-1].append(int(element))
        except csv.Error, e:
            print "CSV error: %s" % e
            return
        except IndexError, e:
            print "Index error: %s" % e
            return

if __name__ == '__main__':
    size = raw_input('Size of graph (positive integer):')
    filename = raw_input('Filename to save to:')
    filename = filename + '.csv'

    graph = Graph(int(size))
    graph.write_to_csv(filename)
