t = int(input())
for k in range(t):
    (p, i) = input().split()
    (p, i) = (int(p), int(i))
    arr = []
    for j in range(p):
        if i >> j & 1:
            arr.append(1)
        else:
            arr.append(0)
    arr = arr[::-1]
    ans = 0
    for j in range(p):
        if arr[j] == 1:
            ans += 2 ** j
    print(ans)
