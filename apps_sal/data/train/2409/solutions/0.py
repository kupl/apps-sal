class Solution:
    def maximum69Number(self, num: int) -> int:
        numString = str(num)
        numLength = len(numString)
        firstIndex = numString.find('6')
        if firstIndex == -1:
            return num
        else:
            return num + 3 * 10**(numLength - firstIndex - 1)
