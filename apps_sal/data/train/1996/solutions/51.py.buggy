class Solution:
    def eventualSafeNodes(self, graph):
        \"\"\"
        :type graph: List[List[int]]
        :rtype: List[int]
        \"\"\"
        n = len(graph)
        res = set([i for i in range(n) if graph[i] == []])
        left = set(range(n)) - res
        while True:
            new_res = set(res)
            new_left = set(left)
            for i in left:
                if set(graph[i]).issubset(res):
                    new_res.add(i)
                    new_left.remove(i)
            if new_res == res:
                return sorted(list(res))
            else:
                res = new_res
                left = new_left
