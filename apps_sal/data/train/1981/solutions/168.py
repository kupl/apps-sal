class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        events = [0]*(10**5+1)
        for start, end in requests:
            events[start] += 1
            events[end+1] -= 1
        for i in range(1, len(events)):
            events[i] += events[i-1]
        events.sort()
        nums.sort()
        modulo = 10**9+7
        answer = 0
        while nums and events:
            answer = (answer+nums.pop()*events.pop())%modulo
        return answer
