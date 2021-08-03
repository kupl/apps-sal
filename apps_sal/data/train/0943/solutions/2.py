T = int(input())
for t in range(T):
    V, W = [int(x) for x in input().split()]
    print(min(V, W) + 1)
