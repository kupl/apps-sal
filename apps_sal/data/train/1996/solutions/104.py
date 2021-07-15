class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        
        out_degree = [0] * n
        
        in_nodes = collections.defaultdict(list) 
        term_nodes = []
        
        for i in range(n):
            
            out_degree[i] = len(graph[i])
            
            if out_degree[i] == 0: 
                term_nodes.append(i)
                
            for j in graph[i]: 
                in_nodes[j].append(i) 
                
        #print(f'out_degree:{out_degree}') #out_degree:[2, 2, 1, 1, 1, 0, 0]
        #print(f'in_nodes:{in_nodes}')  
        #in_nodes:defaultdict(<class 'list'>, {1: [0], 2: [0, 1], 3: [1], 5: [2, 4], 0: [3]})
        #print(f'term_nodes:{term_nodes}')   #term_nodes:[5, 6]

                      
        for term_node in term_nodes:
            for in_node in in_nodes[term_node]:
                
                out_degree[in_node] -= 1
                
                if out_degree[in_node] == 0: 
                    term_nodes.append(in_node)
                    
        return sorted(term_nodes)

