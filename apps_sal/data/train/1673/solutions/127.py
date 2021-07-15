class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        import heapq

        dp = arr[0][:]
        for i in range(1, len(arr)):
            heap = list((v, k) for k, v in enumerate(dp))
            heapq.heapify(heap)
            min_value, min_pos = heapq.heappop(heap)
            alter_value, _ = heapq.heappop(heap)
            new_dp = [v + min_value for v in arr[i]]
            new_dp[min_pos] += alter_value - min_value
            dp = new_dp
        return min(dp)
