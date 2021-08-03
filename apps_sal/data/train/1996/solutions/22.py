class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = collections.defaultdict(int)
        dic = collections.defaultdict(list)
        queue = collections.deque()
        visited, res = set(), []
        for i in range(len(graph)):
            outdegree[i] += len(graph[i])
            if not graph[i]:
                queue.append(i)
                visited.add(i)
            for node in graph[i]:
                dic[node].append(i)

        # print(indegree)
        # print(outdegree)
        # print(dic)
        # print(queue)
        # print('*********')

        while queue:
            node = queue.popleft()
            res.append(node)
            for nbr in dic[node]:
                outdegree[nbr] -= 1
                if nbr not in visited and outdegree[nbr] == 0:
                    queue.append(nbr)
                    visited.add(nbr)
            # print(queue)
        return(sorted(res))
