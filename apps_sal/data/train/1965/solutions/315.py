class Solution:
    def find(self, i:int, nodes_ptrs: List[int]):
        
        ptr = i
        
        ptr_prev = []
        
        while nodes_ptrs[ptr] != ptr:
            ptr_prev.append(ptr)
            ptr = nodes_ptrs[ptr]
        
        for pr in ptr_prev:
            nodes_ptrs[pr] = ptr
        
        return ptr
    
#     def union(self, i:int, j:int, nodes_ptrs:List[int]):
        
#         ptr_i = find(i, node_ptrs)
#         ptr_j = find(j, node_ptrs)
        
#         if(ptr_i == ptr_j): return 0
#         else:
#             nodes_ptrs[ptr_i] = ptr_j
        
#         return ptr_j
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        ANodes = list(range(n+1))
        BNodes = list(range(n+1))
        
        AConnected = {}
        BConnected = {}
        
        AMaxConnect = 1
        BMaxConnect = 1
        
        n_used = 0
        
        edges_traverse = [0]*len(edges)
        
        j = 0
        k = -1
        for i in range(len(edges)):
            if (edges[i][0] == 3):
                edges_traverse[j] = i
                j += 1
            else:
                edges_traverse[k] = i
                k -= 1
        
        for i in range(len(edges_traverse)):
            
            [typei, u, v] = edges[edges_traverse[i]]
            #print(type_i, u_i, vi)
            
            include_A = False
            include_B = False
            
            #Exam Alice
            
            u_ptr_A = self.find(u, ANodes)
            v_ptr_A = self.find(v, ANodes)
            u_ptr_B = self.find(u, BNodes)
            v_ptr_B = self.find(v, BNodes)
            
            
            if typei != 2 and u_ptr_A != v_ptr_A:
                include_A = True
            
            #Exam Bob
            if typei != 1 and u_ptr_B != v_ptr_B:
                include_B = True
            
            include = include_A or include_B
            
            # print(include, n_used)
            
            if (include):
                
                n_used += 1
                
                if(include_A):
                    num_ui_set = AConnected.get(u_ptr_A, 1) 
                    num_vi_set = AConnected.get(v_ptr_A, 1)
                

                    ANodes[u_ptr_A] = v_ptr_A
                    AConnected[v_ptr_A] = num_ui_set + num_vi_set
                    if AConnected[v_ptr_A] > AMaxConnect:
                        AMaxConnect = AConnected[v_ptr_A]
                
                if(include_B):
                    num_ui_set = BConnected.get(u_ptr_B, 1) 
                    num_vi_set = BConnected.get(v_ptr_B, 1)
                
                    BNodes[u_ptr_B] = v_ptr_B
                    BConnected[v_ptr_B] = num_ui_set + num_vi_set
                    if BConnected[v_ptr_B] > BMaxConnect:
                        BMaxConnect = BConnected[v_ptr_B]
                
                if(AMaxConnect == n and BMaxConnect == n): break
            
            # print(BNodes)
            # print(ANodes)
        
        if(AMaxConnect != n or BMaxConnect !=n): return -1
        
        return len(edges)-n_used
            
            

