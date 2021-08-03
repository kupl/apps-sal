t = int(input())
for i in range(t):
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    c = 0
    x = 0
    b = list()
    i1 = 0
    i2 = 0
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
