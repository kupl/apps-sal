# cook your dish here
for i in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c, x, i1, i2, b = 0, 0, 0, 0, list()
    for j in range(n):
        c += 1
        if a[j] > k:
            x += 1
            if x == 1:
                i1 = j
            else:
                if a[j] == a[i1]:
                    x -= 1
                else:
                    i2 = j
        if x == 2:
            x = 1
            b.append(c - 1)
            c = i2 - i1
            i1 = i2
            i2 = 0
        if j == n - 1 and b == []:
            b.append(n)
    print(max(b))
