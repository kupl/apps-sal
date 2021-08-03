t = int(input())
for z in range(t):
    s = input()
    j = 1
    ans = 0
    a = []
    for i in s:
        if i != '=':
            a.append(i)

    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            j += 1
            ans = max(ans, j)
        else:
            j = 1

    print(ans + 1)
