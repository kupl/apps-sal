class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        minRange = len(str(low))
        maxRange = len(str(high))
        digits = ['1','2','3','4','5','6','7','8','9']
        
        result = []
        for n in range(minRange, maxRange + 1):
            for i in range(10-n):
                num = int(''.join(digits[i:i+n]))
                if num >= low and num <= high:
                    result.append(num)
                if num > high:
                    break
        return result
