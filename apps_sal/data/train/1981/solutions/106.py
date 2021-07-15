class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        i_count = Counter()
        first = float('inf')
        last = -first

        for start, end in requests:
            i_count[start] += 1
            i_count[end + 1] -= 1
            first = min(first, start)
            last = max(last, end)

        q = []
        s = 0

        for p in range(first, last + 1):
            s += i_count[p]
            q.append(-s)

        heapq.heapify(q)

        ans = 0
        nums.sort()

        while q:
            ans = (ans + nums.pop() * -heapq.heappop(q)) % 1000000007

        return ans
