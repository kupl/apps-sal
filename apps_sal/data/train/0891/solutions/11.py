from sys import stdin,stdout
def problem():
    n , m = [int(x) for x in stdin.readline().split()]
    for _ in range(m):
        q = int(stdin.readline());l = max(q-n,n+1);r = min(q -1 ,2*n)
        if r >= l:print(r- l + 1)
        else:print(0)
problem()
