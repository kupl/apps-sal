for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(n)
        continue
    s = []
    for i in range(1, n + 1):
        s.append(i)
    s *= 2
    for i in range(0, len(s) // 2):
        x = s[i:i + n]
        x = list(map(str, x))
        print(''.join(x))
