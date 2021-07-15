class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        n = int((num+2)**0.5+1)
        d = num
        res = [1, num]
        for i in range(n, 0, -1):
            if not (num+1)%i: 
                if d>=abs(i - (num+1)//i):
                    res[0], res[1] = i, (num+1)//i
                    d = abs(i - (num+1)//i)
            
            if not (num+2)%i:
                if d>=abs(i - (num+2)//i):
                    res[0], res[1] = i, (num+2)//i
                    d = abs(i - (num+2)//i)
        return res
