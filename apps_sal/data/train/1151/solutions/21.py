# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

viz = [0] * 1005
# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        nonlocal viz
        # Mark the current node as visited
        # and print it
        visited[v] = True
        viz[v] = 1
        # print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v, visited):

        # Mark all the vertices as not visited
        # visited = [False] * (max(self.graph)+1)

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

        return visited

# Driver code


# Create a graph given
# in the above diagram
for _ in range(int(input())):

    g = Graph()
    n, m = list(map(int, input().split()))
    vizi = [False] * (n + 1)
    for i in range(m):
        a, b = list(map(int, input().split()))
        g.addEdge(a, b)
        g.addEdge(b, a)

    cnt = 0
    for i in range(n):
        if vizi[i] == False:
            cnt += 1
            vizi = g.DFS(i, vizi)

    print(cnt)

# print("Following is DFS from (starting from vertex 2)")
# g.DFS(2)

# This code is contributed by Neelam Yadav
