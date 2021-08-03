class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        def closest(i, arr):
            for j in arr:
                if j > i:
                    return j
            return -1

        ans = [1] * len(rains)
        visited = dict()
        zeros = deque()
        x = 0
        while x < len(rains) and rains[x] == 0:
            x += 1

        for i in range(x, len(rains)):
            if rains[i] in visited:
                if not zeros:
                    return []
                else:
                    r = visited[rains[i]]
                    c = closest(r, zeros)
                    if c == -1:
                        return []
                    ans[c] = rains[i]
                    zeros.remove(c)
                    ans[i] = -1
                    visited[rains[i]] = i
            elif rains[i]:
                ans[i] = -1
                visited[rains[i]] = i
            else:
                zeros.append(i)
        return ans
