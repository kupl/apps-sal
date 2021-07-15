from collections import deque
from math import factorial 

def fixed_points_perms(n,m): 
    if m >= n : return [1,0][m>n]
    
    def dear(n):
        arr, i  = deque([1,0,1]), 3 
        while i < n+1 :
            arr.append((i-1)*(arr[-1] + arr[-2]))
            arr.popleft()
            i+=1
        return arr[-1]

    de = [1,0,1][n-m] if n-m<=2  else dear(n-m)

    return (factorial(n)*de)//(factorial(n-m)*factorial(m))
