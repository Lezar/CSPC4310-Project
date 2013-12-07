import math

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
        self.points = [(random.random() *n*n, random.random() *n*n)]        
        for i in range(1,n):
            print i
            metric = False
            # Ensure triangular inequality as each point is added to the list
            # Generate graph matrix while points are being added
            while not metric:
                metric = True
                
                # Use a large range for random to ensure inequalities occur each time
                point = (random.random() *n*n, random.random() *n*n)
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

if __name__ == '__main__':
    graph = Graph(1000)
