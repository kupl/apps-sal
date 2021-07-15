#double underscore makes a class variable or a class method private
mod = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
it = lambda : tuple(map(int, input().split()))
ls = lambda : list(input())
t=ii()
for _ in range(t):
    n=ii()
    l=il()
    mn=l[-1]
    c=0
    for i in range(n-1,-1,-1):
        if l[i]>mn:
            c+=1
        mn=min(mn,l[i])
    print(c)
