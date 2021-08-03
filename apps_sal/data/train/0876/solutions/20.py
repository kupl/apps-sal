T = int(input())
while(T):
    nx = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    if max(A) - min(A) < nx[1]:
        print("YES")
    else:
        print("NO")
    T = T - 1
