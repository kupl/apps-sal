q = int(input())
for _ in range(q):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = []
    last = a[0]
    count = 1
    for i in range(1, n):
        if a[i] != last:
            s.append(count)
            last = a[i]
            count = 0
        count += 1
    s.append(count)
    s.sort()
    answer = s[-1]
    for i in range(len(s) - 2, -1, -1):
        if s[i] >= s[i + 1]:
            s[i] = s[i + 1] - 1
        if not s[i]:
            break
        answer += s[i]
    print(answer)
