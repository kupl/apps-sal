n = int(input())
p = sorted([(-sum(map(int, input().split())), i) for i in range(n)])
for i in range(n):
    if p[i][1] == 0:
        print(i + 1)
        break
