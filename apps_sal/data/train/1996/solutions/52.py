class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph = list(map(set, graph))
        rgraph = defaultdict(set)
        q = deque()

        for i, nn in enumerate(graph):
            if not nn:
                q.append(i)
            for j in nn:
                rgraph[j].add(i)
        res = []
        while q:
            j = q.popleft()
            res.append(j)
            for i in rgraph[j]:
                graph[i].remove(j)
                if not graph[i]:
                    q.append(i)
        res.sort()
        return res

#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         self.nope = set()
#         res = []
#         for i in range(len(graph)):
#             if i in self.nope:
#                 continue
#             if not self.has_cycle(graph, i, i, set()):
#                 res.append(i)
#         return res


#     def has_cycle(self, graph, i, root, seen):
#         # print('here', i, root, seen)
#         if i == root and root in seen:
#             self.nope.add(i)
#             return True
#         if i in seen:
#             self.nope.add(i)
#             return True

#         res = False
#         seen.add(i)
#         for nei in graph[i]:
#             res |= self.has_cycle(graph, nei, root, seen)
#         seen.remove(i)
#         return res
