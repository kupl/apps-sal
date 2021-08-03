class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        highest = sorted(nums, reverse=True)
        pointers = [[0, 0] for _ in range(len(nums))]
        for req in requests:
            pointers[req[0]][0] += 1
            pointers[req[1]][1] += 1
        print(pointers)
        lefts = 0
        rights = 0
        freq = []
        for pointer in pointers:
            lefts += pointer[0]
            freq.append(lefts - rights)
            rights += pointer[1]
        ans = 0
        freq.sort(reverse=True)
        for i in range(len(freq)):

            ans += freq[i] * highest[i]

        mod = 10**9 + 7
        return ans % mod
