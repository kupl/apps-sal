# cook your dish here
t = int(input())
while t > 0:
    a, m = list(map(int, input().split()))
    l = m // a
    arr = []
    for i in range(l, 0, -1):
        if m - i * a > i:
            break
        if m - a * i == 0:
            continue
        elif i % (m - a * i) == 0:
            arr.append(i)
    print(len(arr))
    arr = arr[::-1]
    print(" ".join(map(str, arr)))
    t = t - 1
