# cook your dish here
n, m = list(map(int, input().split()))
k = n + m - 1
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
d = []
c = 0
for i in range(n):
    for j in range(m):
        a = l1[i] + l2[j]
        if a not in d:
            d.append(a)
            print(i, j)
            c += 1

        if c == k:
            break

    if c == k:
        break
