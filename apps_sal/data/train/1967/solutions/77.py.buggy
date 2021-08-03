class Solution:
    def splitIntoFibonacci(self, s: str) -> List[int]:
        result = []
        n = len(s)
        
        self.backtrack(s, 0, n, [], result)
        
        return result
    
    def backtrack(self, s, left, n, currArr, result):        
        if len(currArr) > 2:
            if currArr[-1] != currArr[-2] + currArr[-3]:
                return False
            else:
                if left >= n:
                    result.append(currArr)
                    return True
        
        for i in range(left, n):
            
            if (s[left] == \"0\" and i != left) or int(s[left:i+1]) > (2**31)-1:
                return False
                
            newArr = currArr.copy()
            newArr.append(int(s[left:i+1]))
            
            if (len(newArr) > 2):
                if (newArr[-1] != newArr[-2] + newArr[-3]):
                    continue
            
            res = self.backtrack(s, i+1, n, newArr, result)
            
            if res == True:
                return True
            
