class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        ans = 0
        hp, hp2 = [], []
        n, mina, maxa = len(A), min(A), max(A)
        seen = set()
        for a in A:
            if a not in seen:
                seen.add(a)
            else:
                heapq.heappush(hp, a)
        for i in range(mina + 1, maxa + n):
            if i not in seen:
                heapq.heappush(hp2, i)
        while hp:
            while hp2[0] <= hp[0]:
                heapq.heappop(hp2)
            ans += heapq.heappop(hp2) - heapq.heappop(hp)
        return ans
