import string
for _ in range(int(input())):
    s, k = list(map(str, input().split()))
    k = int(k)
    lower = [i for i in string.ascii_lowercase]
    l = {}
    for i in lower:
        l[i] = 0
    for i in s:
        l[i] += 1
    ans = len(s)
    for i in lower:
        c = 0
        for j in lower:
            if l[j] < l[i]:
                c += l[j]
            elif (l[j] - l[i]) > k:
                c += l[j] - l[i] - k
        ans = min(ans, c)
    print(ans)
