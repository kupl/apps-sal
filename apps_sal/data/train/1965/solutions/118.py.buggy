class Graph:
    def __init__(self):
        self.vertices = set()
        self.bi_edges = set()
        self.uni_edges = set()
    
    def find(self, parent, u):
        if parent[u] == u:
            return u
        return self.find(parent, parent[u])
    
    
    def union(self, parent, rank, u, v):
        
        u_root = self.find(parent, u)
        v_root = self.find(parent, v)
        
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
        return 0
        

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        print(\"total edges\", len(edges))
        # print(sorted(edges, key=lambda x : x[0]))
        graph1 = Graph()
        graph2 = Graph()
        
        #create 2 graphs
        for edge in edges:
            edge_type = edge[0]
            u = edge[1]
            v = edge[2]
            
            if edge[0]==1:
                graph1.vertices.add(u)
                graph1.vertices.add(v)
                graph1.uni_edges.add((u,v))
            elif edge[0] == 2:
                graph2.vertices.add(u)
                graph2.vertices.add(v)
                graph2.uni_edges.add((u,v))
            else:
                graph1.vertices.add(u)
                graph1.vertices.add(v)
                graph1.bi_edges.add((u,v))
                
                graph2.vertices.add(u)
                graph2.vertices.add(v)
                graph2.bi_edges.add((u,v))
        
        if len(graph1.vertices) < n or len(graph2.vertices) < n:
            return -1
        
        
        print(\"edges in graph\",len(graph1.bi_edges)+len(graph1.uni_edges)+len(graph2.uni_edges))
        deleted = 0

        #detect cycle for given graph
        # return count of deleted uni_edges and cycle_creating bi_edges
        def minimum_spanning_tree(graph):
            parent = {}
            rank = {}
            
            for node in range(1,n+1):
                parent[node] = node
                rank[node] = 0
            
            cycle_bi_edges = set()
            for edge in graph.bi_edges:
                u = edge[0]
                v = edge[1]
                
                if graph.find(parent, u) != graph.find(parent, v):
                    graph.union(parent, rank, u, v)
                else:
                    cycle_bi_edges.add(edge)
            
            delete = 0
            for edge in graph.uni_edges:
                u = edge[0]
                v = edge[1]
                
                if graph.find(parent, u) != graph.find(parent, v):
                    graph.union(parent, rank, u, v)
                else:
                    delete += 1
            # print(\"span\", delete, len(cycle_bi_edges))
            return delete, cycle_bi_edges
        
        result1 = minimum_spanning_tree(graph1)
        
        result2 = minimum_spanning_tree(graph2)
        
        deleted = deleted + result1[0] + result2[0]
        
        delete_bi = 0
        for edge in result1[1]:
            u = edge[0]
            v = edge[1]
            
            if (u,v) in result2[1]:
                delete_bi += 1
            
            if (v,u) in result2[1]:
                delete_bi +=1
        print(delete_bi)
        return deleted+delete_bi
                
                
                
            
        
