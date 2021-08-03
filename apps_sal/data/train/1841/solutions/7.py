class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)

        arr.sort()
        median = arr[(N - 1) // 2]

        heap = []
        for n in arr:
            heapq.heappush(heap, (-abs(n - median), -n, n))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[-1])
        return ans
