T = int(input())
for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    if (sum(l) < 0):
        print("NO")
    else:
        print("YES")
