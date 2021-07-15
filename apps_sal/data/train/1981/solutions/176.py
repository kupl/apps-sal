class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        stream = []
        for start, end in requests:
            stream.append((start, 0))
            stream.append((end, 1))
        stream.sort()
        
        multiples = []
        cur_count = 0
        cur_event = 0
        for i in range(len(nums)):
            while cur_event < len(stream) and i == stream[cur_event][0] and stream[cur_event][1] == 0:
                cur_count += 1
                cur_event += 1
            multiples.append(cur_count)
            while cur_event < len(stream) and i == stream[cur_event][0] and stream[cur_event][1] == 1:
                cur_count -= 1
                cur_event += 1
        
        multiples.sort(reverse=True)
        nums.sort(reverse=True)
        
        return sum(num * multiple for num, multiple in zip(nums, multiples)) % (10**9 + 7)
