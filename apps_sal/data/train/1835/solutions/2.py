class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        
        ans = []
        
        for num in range(1, 10):
            self.dfs(n-1, num, ans, k)
        
        return ans
    
    def dfs(self, n, num, ans, k):
        if n == 0:
            return ans.append(num)
        
        last_digit = num % 10
        
        next_ds = set([last_digit + k, last_digit - k])
        
        for digit in next_ds:
            if 0 <= digit < 10:
                tmp = num * 10 + digit
                self.dfs(n-1, tmp, ans, k)


