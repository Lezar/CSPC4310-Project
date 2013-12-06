import math
import graph
import random

def distance(point1, point2):
    """Find the distance between two points and return it as an integer"""
    return int(math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2))
        
class Graph():
    """Generate complete metric graph as a 2D list (matrix) to be used for k-centre

    Constructor Arguments:
    n (int): The number of vertices in the graph 

    Attributes:
    graph (list): A complete metric graph represented as a 2D list
                  Each entry (i,j) in the array represents the distance between vertices indexed i and j
    
    """

    def __init__(self, n=1):
        self.graph = [[0]*n]*n
        print "Graph of Size %s" % (n,)
        for row in self.graph:
            print row

