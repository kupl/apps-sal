t=int(input())
for i in range(t):
    a=int(input())
    b=[int(b) for b in input().split()]
    b.sort()
    for j in range(len(b)):
        if b[j]==0 and b[j+1]==1:
            print(j+1)
            break
