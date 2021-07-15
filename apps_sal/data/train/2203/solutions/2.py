n = int(input())
for i in range(n):
    k = list(map(int, input().split()))
    if len(set(k)) == n:
        k[k.index(0)] = n
        print(*k)
        break
