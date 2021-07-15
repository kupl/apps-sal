class Solution:
    def numberOfSteps (self, num: int) -> int:
        bnum = bin(num)
        return len(bnum) + bnum.count('1') - 3
