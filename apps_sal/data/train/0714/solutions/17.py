# cook your dish here
a = int(input())
z = []
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    p = 0
    if sum(c) % b != 0:
        p = p + b - (sum(c) % b)
        q = int(sum(c) / b) + 1
    else:
        q = int(sum(c) / b)

    for j in c:
        if j > q:
            p = p + j - q
    z.append(p)
for i in z:
    print(i)
