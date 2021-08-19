T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    W = [int(i) for i in input().split()]
    for i in range(N):
        W[i] += i
    ans.append(max(W))
for i in ans:
    print(i)
