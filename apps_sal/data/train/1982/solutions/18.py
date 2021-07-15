from collections import defaultdict, deque

class Solution:
    # Time: O(E) | Space: O(V+E)
    def create_adjacency_list(self, dislikes):
        adjacency_list = defaultdict(list)
        # undirected graph (a dislikes b -> b also dislikes a)
        for i , j in dislikes:
            adjacency_list[i].append(j) # since vertices numbered from 1 to N
            adjacency_list[j].append(i) # imp for undirected graph
        return adjacency_list
    
    # BFS solution
    # Time: O(V+E) | Space: O(V+E)
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # create adjacency list
        adjacency_list = self.create_adjacency_list(dislikes)
        
        print(adjacency_list)
        
        # initialize colors ( for bipartite segregation, alos serves as visited flag)
        color = {vertex:-1 for vertex in adjacency_list}
        print(color)
        
        # initialize bfs queue
        queue = deque()
        
        # call bfs on every connected component
        for vertex in adjacency_list: # remember - adjacency_list is a dict
            if color[vertex] == -1:
                # bfs
                # color the source (visited) add it to queue 
                color[vertex] = 0
                queue.append(vertex)
                
                # main bfs loop
                while queue:
                    current_node = queue.popleft()
                    for neighbor in adjacency_list[current_node]:
                        if color[neighbor] == color[current_node]:
                            return False
                        if color[neighbor] == -1:
                            # not colored (visited)
                            # color of neighbor should be opposite of current node for it to be bipartite
                            # color the neighbor and add it to queue
                            color[neighbor] = 1-color[current_node]
                            queue.append(neighbor)
            
        # if we reach here we have a valid bipartite graph
        return True
                            
                    
        
        

