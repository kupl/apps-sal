# cook your dish here
t = int(input())

for _ in range(t):
    l = []
    n = int(input())
    temp = list(map(int, input().split()))
    l = temp[n - 2: n]
    l.extend(temp)
    l.extend(temp[: 3])
    tx = sum(l[:3])
    mx = tx
    for i in range(3, len(l)):

        mx = max(mx, tx - l[i - 3] + l[i])
        tx = tx - l[i - 3] + l[i]

    print(mx)
