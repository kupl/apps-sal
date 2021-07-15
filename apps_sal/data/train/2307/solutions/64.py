from sys import stdin, setrecursionlimit
import bisect,collections,copy,itertools,math,string
setrecursionlimit(10**9)

def input():
    return stdin.readline().strip()
        
def main():

    n, a, b = list(map(int, input().split()))
    x = list(map(int, input().split()))

    ans = 0
    for i in range(n-1):
        ans += min((x[i+1]-x[i])*a, b)
    
    print(ans)



def __starting_point():
    main()

__starting_point()
