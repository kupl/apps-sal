from collections import deque, defaultdict
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rq = defaultdict(deque)
        for i, r in enumerate(rains):
            rq[r].append(i)
        for r, q in list(rq.items()):
            q.popleft()
        ans = [-1] * len(rains)
        urgent = []
        for i, r in enumerate(rains):
            if r != 0:
                q = rq[r]
                if q:
                    heapq.heappush(urgent, q.popleft())
            elif urgent:
                d = heapq.heappop(urgent)
                if d < i:
                    return []
                ans[i] = rains[d]
            else:
                ans[i] = 1
        return ans if not urgent else []
