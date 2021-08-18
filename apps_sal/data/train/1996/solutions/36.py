class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        out_degree = collections.defaultdict(int)
        inward_nodes = collections.defaultdict(list)

        for src in range(len(graph)):
            for child in graph[src]:
                inward_nodes[child].append(src)
                out_degree[src] += 1

        q = collections.deque()
        for i in range(len(graph)):
            if not i in out_degree:
                q.append(i)

        result = []
        while q:
            top = q.popleft()
            result.append(top)
            for parent in inward_nodes[top]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    q.append(parent)
        return sorted(result)
