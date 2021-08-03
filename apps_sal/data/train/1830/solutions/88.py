class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        nex = [-1] * len(rains)
        last = {}
        for i, n in enumerate(rains):
            if n in last:
                nex[last[n]] = i
            last[n] = i

        prio, answer = [], []
        for i, event in enumerate(rains):
            if prio and prio[0] <= i:
                return []

            if event != 0:
                if nex[i] != -1:
                    heapq.heappush(prio, nex[i])
                answer.append(-1)
            else:
                answer.append(rains[heapq.heappop(prio)] if prio else 1)

        return answer
