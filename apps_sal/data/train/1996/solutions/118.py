import collections\r
class Solution:\r
    def eventualSafeNodes(self, graph):\r
        q = collections.deque()\r
        outdegree = [0]*len(graph)\r
        income_node = collections.defaultdict(list)\r
        result = []\r
        for i in range(len(graph)):\r
            outdegree[i] = len(graph[i])\r
            if outdegree[i] == 0:\r
                q.append(i)\r
                continue\r
            for next_node in graph[i]:\r
                income_node[next_node].append(i)\r
        \r
        while q:\r
            node = q.popleft()\r
            result.append(node)\r
            for pre_node in income_node[node]:\r
                outdegree[pre_node] -= 1\r
                if outdegree[pre_node] == 0:\r
                    q.append(pre_node)\r
        \r
        return sorted(result)\r
\r
def __starting_point():\r
    sol = Solution()\r
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]\r
    sol.eventualSafeNodes(graph)\r
\r
\r
\r
        \r
\r
                \r
\r
\r
        
__starting_point()
