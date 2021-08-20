(n, q) = map(int, input().split())
f = [int(w) for w in input().split()]
ft = []
ft.append(f[0])
for i in range(1, n):
    temp = ft[i - 1]
    temp = temp ^ f[i]
    ft.append(temp)
ft.append(0)
while q:
    k = int(input())
    index = k % (n + 1) - 1
    print(ft[index])
    q = q - 1
