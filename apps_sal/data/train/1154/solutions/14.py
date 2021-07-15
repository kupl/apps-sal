# cook your dish here
def solve():

    n=int(input())
    k=list(map(int,input().split()))
    h=list(map(int,input().split()))
    k.sort()
    h.sort()
    flag=0
    for i in range(n):
        if k[i] != h[i]:
            print(h[i])
            flag=1
            break
    if flag==0 :
        print(h[-1])
t = 1
for i in range(t):
    solve()
