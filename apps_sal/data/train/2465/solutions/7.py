class Solution:
    def divisorGame(self, n: int) -> bool:
        return self.helper(n, {})
    
    def helper(self, n, memo):
        if n == 1:
            return False
        elif n in memo:
            return memo[n]
        else:
            for f in self.factors(n):                
                if self.helper(n-f, memo) == False:
                    memo[n] = True
                    return True
            memo[n] = False
            return False
        
    def factors(self, n):
        l = []
        i = 1
        while i**2 <= n:
            if n % i == 0:
                l.append(i)
            i += 1
        for num in l:
            if num**2< n and num > 1:
                l.append(int(n/num))
                
        return l
