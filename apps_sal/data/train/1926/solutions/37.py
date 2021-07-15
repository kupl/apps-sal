class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a,b = None,None
        minDiff = float('inf')
        for i in range(1,int(num**(1/2))+10):
            if (num+1) % i == 0:
                cand1 = i
                cand2 = (num+1) // i
                if abs(cand1-cand2) < minDiff:
                    a,b = cand1,cand2
                    minDiff = abs(cand1-cand2)
            if (num+2) % i == 0:
                cand1 = i
                cand2 = (num+2) // i
                if abs(cand1-cand2) < minDiff:
                    a,b = cand1,cand2
                    minDiff = abs(cand1-cand2)
        return [a,b]
