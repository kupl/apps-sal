class Solution:
    dp = dict()
    def rec(self, start, finish, fuel, loc):
        nonlocal dp
        if (start, fuel) in dp:
            return dp[(start, fuel)]
        if fuel<0:
            dp[(start, fuel)] = 0
            return dp[(start, fuel)]
        ans = 0
        if start==finish:
            ans+=1
        for i in range(len(loc)):
            if i==start:
                continue
            ans+=self.rec(i,finish,fuel-abs(loc[start]-loc[i]),loc)
        dp[(start, fuel)] = ans
        return dp[(start, fuel)]
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        nonlocal dp
        dp = dict()
        return (self.rec(start, finish, fuel, locations))%(1000000007)
