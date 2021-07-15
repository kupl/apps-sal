class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        m = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                cost = abs(locations[i]-locations[j])
                m[i][j] = cost
                m[j][i] = cost
        mod = int(1e9+7)
        memo = [[-1 for i in range(n)] for j in range(fuel+1)]
        def DFS(start,finish,f):
            if memo[f][start]!=-1:
                return memo[f][start]
            if f<0:
                return 0
            res = 0
            if start==finish:
                res +=1
            for i in range(n):
                if i!=start and m[start][i]<=f:
                    res =(res+ DFS(i,finish,f-m[start][i]))%mod
            memo[f][start]  = res
            return res
        return DFS(start,finish,fuel)
            
        

