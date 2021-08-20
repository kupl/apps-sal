t = int(input())
for i in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    l = 0
    s = lst[0]
    for j in range(1, len(lst)):
        if s >= 1:
            l += 1
            s -= 1
            s += lst[j]
        else:
            break
    ans = l + s
    print(ans)
