class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        ans = 0
        c = Counter(A)
        backlog = 0
        for i in range(min(A), max(A)+1):
            if i in c:
                backlog += c[i] - 1
            elif i not in c and backlog:
                ans += i
                backlog -= 1
        ans += sum(range(i+1, i+1+backlog))       
        return sum(c.keys()) + ans - sum(A)
        
        

