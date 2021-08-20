T = int(input())
ans = []
m = 10 ** 9 + 7
for _ in range(T):
    N = [int(i) for i in input().split()]
    N.sort()
    ans.append(N[0] % m * ((N[1] - 1) % m) * ((N[2] - 2) % m) % m)
for i in ans:
    print(i)
