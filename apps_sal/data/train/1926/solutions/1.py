class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num+=2 #so values are num and num-1
        i = int(math.sqrt(num))
        while i>1:
            r = num%i
            if r<=1:
                return [i,(num-r)//i]
            i-=1
        return [1, num-1]
