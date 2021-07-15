class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo={}
        n=len(locations)
        def dfs(cur,i):
            if cur<0:
                return 0
            if (cur,i) not in memo:
                ans=0
                if i==finish and cur>=0:
                    ans+=1
                for j in range(n):
                    if j==i:
                        continue
                    ans+=dfs(cur-abs(locations[i]-locations[j]),j)
                    ans%=10**9 + 7
                memo[(cur,i)]=ans
            return memo[(cur,i)]
        return dfs(fuel,start)
        
                

