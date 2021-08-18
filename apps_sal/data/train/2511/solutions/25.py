class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        check = set()
        for num in A:
            if num in check:
                return num
            check.add(num)
