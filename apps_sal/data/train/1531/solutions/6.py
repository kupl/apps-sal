N = int(input())
branch = list(map(int,input().split()))
t = int(input())
for i in range(t):
    x, y = list(map(int,input().split()))
    if(x==1):
        try:
            branch[x] += branch[x-1] - y
        except:
            pass
    else:
        try:
            branch[x-2] += y - 1
        except:
            pass
        try:
            branch[x] += branch[x-1] - y
        except:
            pass
    branch[x-1] = 0
for j in branch:
    print(j)

