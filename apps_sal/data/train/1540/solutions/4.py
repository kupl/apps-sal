T = int(input())
while T>0:
    N = int(input())
    K = int(input())
    if K %N ==0:
        print("YES")
    else:
        print("NO")
    T = T-1
