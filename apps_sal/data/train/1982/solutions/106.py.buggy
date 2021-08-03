class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(s):
            nonlocal doable
            visited[s] = 1
            for w in adjlist[s]:
                if visited[w] == -1:
                    visited[w] = 1
                    parent[w] = s
                    color[w] = 1 - color[s]
                    dfs(w)
                else:
                    if w != parent[s]:
                        # Odd-length cycles in graph are not amicable, but even-length cycles are ok.
                        # In dfs, back-edge having same color is sign of impossible 
                        # In BFS cross-edge across consecutive levels is ok, but not on the same level.
                        # The distance[] helps to decide this
                        if color[w] == color[s]:
                            doable = False
        n = N 
        doable = True
        visited = {x:-1 for x in range(1,n+1)}
        parent = {x:None for x in range(n)}
        # adjlist = {x:[] for x in range(1,n+1)}
        adjlist = {x:set() for x in range(1,n+1)}
        for dislike in dislikes:
            [s,d] = dislike
            # adjacency-list implementation
            # adjlist[d].append(s)
            # adjlist[s].append(d)
            # adjacency-map implementation 
            # https://algocoding.wordpress.com/2014/08/24/adjacency-list-representation-of-a-graph-python-java/
            adjlist[d].add(s)
            adjlist[s].add(d)
            # adjlist[d].setdefault(s,2)
            # adjlist[s].setdefault(d,1)
        color = {x:0 for x in range(n)}
        print(\"adjlist is {}\".format(adjlist))
        for i in range(1,n):
            if visited[i] == -1:
                dfs(i)
        return doable
        
                        
                    
