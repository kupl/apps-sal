class Solution:
    def closestDivisors(self, n: int) -> List[int]:
        def myfunc(n):
            for i in range(int(n**0.5),0,-1):
                if n%i == 0:
                    return [i,n//i]
        x,y=myfunc(n+1),myfunc(n+2)
        return x if abs(x[1]-x[0]) < abs(y[0]-y[1]) else y
