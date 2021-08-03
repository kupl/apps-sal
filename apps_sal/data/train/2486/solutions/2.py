class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(bin(num)) + bin(num).count('1') - 3
