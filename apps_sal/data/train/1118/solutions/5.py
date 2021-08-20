t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s1 = ''
    s0 = ''
    for i in range(n):
        s1 += str(i % 2)
        s0 += str((i + 1) % 2)
    count1 = 0
    count0 = 0
    for i in range(n):
        if s[i] != s1[i]:
            count1 += 1
        if s[i] != s0[i]:
            count0 += 1
    print(min(count1, count0))
