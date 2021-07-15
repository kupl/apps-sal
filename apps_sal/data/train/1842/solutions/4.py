class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        ans= None
        graph= defaultdict(set)
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)


        vis=set([1])

        def  dfs(root,prev_prob,t):
            nonlocal ans
            if  t < 0 : return 
            can = graph[root] - vis

            if root== target:
                ans = prev_prob if not can or t== 0 else 0
                return 
            for x in can:
                if x not in vis:
                    vis.add(x)
                    dfs(x,prev_prob * 1.0 / len(can),t-1)
                if ans is not None : return
        dfs(1,1,t)
        return 0 if ans is None else ans
