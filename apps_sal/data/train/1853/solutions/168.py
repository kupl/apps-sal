def init_graph(edges, n): 
    graph = [[] for _ in range(n)]
    for src, dest, weight in edges: 
        graph[src].append((dest, weight))
        graph[dest].append((src, weight))
    return graph

def run_bfs(src, graph, threshold, n): 
    q = [(0, src)]
    distances = [math.inf for i in range(n)]
    distances[src] = 0
    res = 0
    while(q): 
        distance, node = heapq.heappop(q)
        edges = graph[node]
        print(\"Visiting: \" + str(node))
        for nbr_node, weight in edges: 
            updated_distance = distance + weight
            if distances[nbr_node] > updated_distance and updated_distance<=threshold: 
                print(\"Neighbor: \" + str(nbr_node) + \" distance: \" + str(updated_distance))
                if distances[nbr_node] == math.inf: 
                    print(\"Updating for: \" + str(nbr_node))
                    res = res + 1
                distances[nbr_node] = updated_distance
                heapq.heappush(q, (updated_distance, nbr_node))
    print(\"Returning: \" + str(res))
    return res 

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        if n==0 or not edges: 
            return -1
        
        graph = init_graph(edges, n)
        min_nbrs = math.inf
        min_nbrs_city = -1
        for i in range(n): 
            num_nbrs = run_bfs(i, graph, distanceThreshold, n)
            if num_nbrs <= min_nbrs: 
                min_nbrs = num_nbrs
                min_nbrs_city = max(min_nbrs_city, i)
            
        return min_nbrs_city 
    
    
    
        
            
