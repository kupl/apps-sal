class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        result = [-1] * n

        redDict = defaultdict(list)

        for edge in red_edges:
            redDict[edge[0]].append(edge[1])

        blueDict = defaultdict(list)

        for edge in blue_edges:
            blueDict[edge[0]].append(edge[1])

        queue = deque()

        queue.append((0, 'blue', 0))
        queue.append((0, 'red', 0))
        # result[0] = 0

        while queue:
            item = queue.popleft()
            if result[item[0]] == -1 or result[item[0]] >= item[2]:
                result[item[0]] = item[2]
            if item[1] == 'blue':
                nextColor = 'red'
                nextNodes = blueDict[item[0]]
            else:
                nextColor = 'blue'
                nextNodes = redDict[item[0]]

            for nex in range(len(nextNodes)):
                if nextNodes[nex] != -1:
                    queue.append((nextNodes[nex], nextColor, item[2] + 1))
                    nextNodes[nex] = -1

        return result
