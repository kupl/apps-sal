class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        M = max(rains)
        ans = [-1] * n

        l = set()

        r = collections.defaultdict(list)
        for j in range(n):
            if rains[j] > 0:
                r[rains[j]] += [j]

        i = 0
        tbd = []

        while(i < n):
            if rains[i] > 0:
                if rains[i] in l:
                    return []
                else:
                    l.add(rains[i])
                    r[rains[i]].pop(0)

                    if len(r[rains[i]]) > 0:
                        heapq.heappush(tbd, r[rains[i]][0])

            elif rains[i] == 0:
                if len(tbd) > 0:
                    get = heapq.heappop(tbd)
                    ans[i] = rains[get]
                    l.remove(rains[get])

                else:
                    ans[i] = M + 1
            i += 1

        return ans
