T = int(input())
for i in range(T):
    s = input().strip()
    ini = 1
    for j in range(len(s)):
        ini *= 2
        if j % 2 == 0:
            if s[j] == 'r':
                ini += 2
        elif s[j] == 'l':
            ini -= 1
        else:
            ini += 1
        ini %= 10 ** 9 + 7
    print(ini % (10 ** 9 + 7))
