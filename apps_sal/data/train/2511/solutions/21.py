class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        tracker = set()
        for num in A:
            if not num in tracker:
                tracker.add(num)
            else:
                return num
