\"\"\"
12:09

first construct the graph

generate shortest paths (within threshold) to each city from each city
return the city with the smallest number of paths (and largest number for tiebreak)

iterate thru cities
0
keep a PQ of the shortest distances to each node
when we arrive at a new node, add the node + distance to queue
0->1
1: 2

0->4
4: 8

1->2
2: 3 + 2
1->4
4: min(8, 2 + 2) = 4

continue until the queue is empty. O(E)

at the end of the traversal, remove all nodes from the list of paths for which dist > threshold O(V)

do this for each vertex in the graph
O((E + V)) * V)

Output: iterate through each list of cities, track min number of cities and choose the largest numbered city with the min.

\"\"\"
from collections import defaultdict, deque
import heapq

class Solution:
    def construct_graph(self, n, edges, thresh):
        graph = defaultdict(dict)
        # Don't need to include the edge if it's greater than the threshold
        for src, dst, weight in edges:
            if weight <= thresh:
                graph[src][dst] = weight
                graph[dst][src] = weight
        return graph
    
    def compute_distances(self, n, city, graph, thresh):
        remain = set(range(n))
        pq = [(city, 0)]
        distances = [float('inf')] * n
        distances[city] = 0
        neighbors = []
        
        # Perform dijkstra's to every other city in the graph
        while pq:
            curr, dist = heapq.heappop(pq)
            
            # Update distances to neighbors
            for adj, weight in graph[curr].items():
                temp = weight + dist
                if temp < distances[adj]:
                    distances[adj] = temp
                    heapq.heappush(pq, (adj, temp))
        
        # Return all nodes that are within the distance threshold
        for neighbor, dist in enumerate(distances):
            if neighbor != city and dist <= thresh:
                neighbors.append(neighbor)
                
        return neighbors
        
            
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = self.construct_graph(n, edges, distanceThreshold)
        neighbors = {}
        
        # Compute each city's distances to each neighboring city
        for city in range(n):
            neighbors[city] = self.compute_distances(n, city, graph, distanceThreshold)
        
        # print(graph, neighbors)
        min_cities = len(neighbors[0])
        correct_city = 0
        
        # Find the city with smallest number of neighbors
        for city in range(1, n):
            # print(min_cities, correct_city)
            if len(neighbors[city]) <= min_cities:
                min_cities = len(neighbors[city])
                correct_city = city
        
        return correct_city
        
