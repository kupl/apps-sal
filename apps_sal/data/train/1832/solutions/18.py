class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        
        #Create graph using dictioary of dictioary
        g=collections.defaultdict(dict)
        for edge in edges:
            g[edge[0]][edge[1]]=edge[2]+1
            g[edge[1]][edge[0]]=edge[2]+1
            
        #Use negative move to apply max-heap
        hq=[(-M,0)]*len(g[0])  #The move can be taken together for all outgoing edges
        
        if(len(hq)==0):  #There is no outgoing edges, it can visited minimum of 1
            return 1
        
        #Use the dictionary to store the max remaining moves at this node
        #This will make sure it will cover as many nodes as possible
        visited={}
        
        while hq:
            #Pop out the node with the highest remaining move
            rem_move,node=heapq.heappop(hq)
            if(node in visited):
                continue

            visited[node]=rem_move
            
            for nei in list(g[node].keys()):
                weight=g[node][nei]
                if(nei not in visited and (rem_move+weight)<=0):  #make this move if it satisfies
                    #Don't update visited in this loop, becuase it can only be update after heappop
                    heapq.heappush(hq,(rem_move+weight,nei))

        #Count the number of nodes covered
        res=len(visited)
        
        counted=set()
        #Go through all edges 
        for edge in edges:
            edge_tuple=(min(edge[:2]),max(edge[:2]))
            if(edge[0] in visited and edge[1] in visited and edge_tuple not in counted):
                counted.add(edge_tuple)  #Avoid double couting the same edge
                res+=min(g[edge[0]][edge[1]]-1,-(visited[edge[0]]+visited[edge[1]]))
            elif(edge[0] in visited):
                res=res+(-visited[edge[0]])
            elif(edge[1] in visited):
                res=res+(-visited[edge[1]])
                
        return res
    
        
        
        
        
        
            
            

