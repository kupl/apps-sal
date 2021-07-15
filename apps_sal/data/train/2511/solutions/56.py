class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        j = set()
        for num in A:
            if num in j:
                return num
            else:
                j.add(num)
        return False

