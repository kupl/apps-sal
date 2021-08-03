class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = dict()
        for i in range(len(s)):
            graph[i]=set()
            
        for pair in pairs:
            fro = pair[0]
            to = pair[1]
            graph[fro].add(to)
            graph[to].add(fro)
            
        def dfs(node, graph,explored,s,path):
            path.append(node)
            explored[node]=True
            string = s[node]
            
            for neighbour in graph[node]:
                if not explored[neighbour]:
                    res = dfs(neighbour,graph,explored,s,path)
                    string+=res[0]
                    
            return (string,path)
        
        connected=[]
        explored = [False]*len(s)
        
        for node in graph:
            if not explored[node]:
                connected.append(dfs(node,graph,explored,s,[]))
                
                
            
        stringList = [\"\"]*len(s)
        
        for conn in connected:
            st = \"\".join(sorted(conn[0]))
            path = sorted(conn[1])
            
            for i in range(len(st)):
                char = st[i]
                ind = path[i]
                stringList[ind]=char
                
        return \"\".join(stringList)
                
            
        
                
        
                
            
