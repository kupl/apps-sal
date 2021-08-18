class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n, g = len(grid), len(grid[0]), collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[grid[i][j]] += [complex(i, j)]

        def f(b, s):
            nonlocal time
            time += 1
            boxToTarget = b - target
            return (abs((boxToTarget.real)) + abs((boxToTarget).imag) + s, abs(boxToTarget), time)

        player, box, target, time = *g['S'], *g['B'], *g['T'], 1
        floor = {player, box, target, *g['.']}

        alpha = [(f(box, 1), 1, player, box)]
        directions, visited = (1, -1, 1j, -1j), set()

        low = dict.fromkeys(floor, 0)
        dfn = low.copy()
        count = 0
        index = {}

        def tarjan(currIndex, parentIndex):
            nonlocal count
            count += 1
            dfn[currIndex] = low[currIndex] = count
            index[count] = currIndex
            for direction in directions:
                nextIndex = currIndex + direction
                if nextIndex in floor and nextIndex != parentIndex:
                    if not low[nextIndex]:
                        tarjan(nextIndex, currIndex)
                    low[currIndex] = min(low[currIndex], low[nextIndex])

        tarjan(box, -1)
        for currIndex in floor:
            connect = [currIndex]
            while dfn[connect[-1]] != low[connect[-1]]:
                connect.append(index[low[connect[-1]]])
            for w in connect[:-2]:
                low[w] = low[connect[-1]]

        if not low[player] * low[target]:
            return -1

        while alpha:
            _, steps, currPlayer, currBox = heapq.heappop(alpha)
            for direction in directions:
                nextPlayer, nextBox = currBox - direction, currBox + direction
                if nextBox in floor and nextPlayer in floor and (nextPlayer, currBox) not in visited and low[currPlayer] == low[nextPlayer]:
                    if nextBox == target:
                        return steps
                    heapq.heappush(alpha, (f(nextBox, steps + 1), steps + 1, currBox, nextBox))
                    visited.add((nextPlayer, currBox))
        return -1
