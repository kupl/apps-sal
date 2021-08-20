r = int(input())
for z in range(r):
    s = input()
    s = s.replace('=', '')
    l = list(s)
    final = 0
    ans = 0
    if len(l) == 0:
        print(1)
    else:
        for i in range(1, len(l)):
            if l[i] == l[i - 1]:
                ans = ans + 1
            else:
                if final < ans:
                    final = ans
                ans = 0
        if final < ans:
            final = ans
        print(final + 2)
