class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        weights = defaultdict(int)
        requests.sort()
        (prev, ends) = (requests[0][0], [requests[0][1]])
        for (l, r) in requests[1:]:
            while ends and ends[0] < l:
                weight = len(ends)
                end = heappop(ends)
                weights[weight] += end - prev + 1
                prev = end + 1
            if not ends:
                prev = l
                ends = [r]
            else:
                weight = len(ends)
                weights[weight] += l - prev
                prev = l
                heappush(ends, r)
        while ends:
            weight = len(ends)
            end = heappop(ends)
            weights[weight] += end - prev + 1
            prev = end + 1
        total = 0
        nums.sort(reverse=True)
        l = 0
        for weight in sorted(list(weights.keys()), reverse=True):
            length = weights[weight]
            total += sum(nums[l:l + length]) * weight % MOD
            l = l + length
        return total % MOD
