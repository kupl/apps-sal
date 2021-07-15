class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        diff = math.inf
        ans = []
        n = num
        num = n+1
        
        def func(num):
            nonlocal diff, ans
            
            for i in range(1, math.ceil(math.sqrt(num))+1):
                if num%i == 0:
                    j = num//i
                    if abs(i - j) < diff:
                        diff = abs(i - j)
                        ans = [i, j]
            return ans
        
        func(n + 1)
        func(n + 2)
        
        return ans
