def ceil(num):
    if num % 1 == 0:
        return int(num // 1)
    else:
        return int(num // 1 + 1)


for _ in range(int(input())):
    n = int(input())
    s = input()
    p = 0
    a = []
    for i in range(n):
        if s[i] == 'P':
            p = p + 1
    req = ceil(0.75 * n)
    requirement = req - p
    for i in range(2, n - 2):
        if s[i] == 'A':
            if (s[i - 1] == 'P' or s[i - 2] == 'P') and (s[i + 1] == 'P' or s[i + 2] == 'P'):
                a.append(i)
    if requirement > len(a):
        print(-1)
    else:
        print(max(requirement, 0))
