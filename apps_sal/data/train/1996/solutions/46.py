class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node):
            # if
            # print(\"node\",node)
            if(node in terminalnodes):
                return True
            if(node in visited):
                return False
            visited[node] = 1
            a = True
            for newnodes in graph[node]:
                a = a and dfs(newnodes)
                
            if(a==True):
                terminalnodes.add(node)
                return True
            else:
                return False
        
        
        
        
        nodes = len(graph)
        
        m = []
        # print(len(m))
        
        nonlocal terminalnodes
        terminalnodes = {i for i in range(nodes) if len(graph[i])==0}
        print(terminalnodes)
        nonlocal visited
        visited = {}
        for i in range(len(graph)):
            visited = {}
            a = dfs(i)
            if(a==True):
                terminalnodes.add(i)
        if(len(terminalnodes)==0):
            return []
        
        t = list(terminalnodes)
        t.sort()
        return t   

