class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        num = \"123456789\"
        res = []
        
        for i in range(len(str(low)), len(str(high))+1):
            for j in range(10-i):
                if low <= int(num[j:j+i]) <= high:
                    res.append(int(num[j:j+i]))
        
        return res
        
        
        
