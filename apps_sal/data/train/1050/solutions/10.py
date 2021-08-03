t = int(input())
while t:
    a = list(map(str, input()))
    b = []
    c, ans = 0, 0
    for i in range(len(a)):
        if a[i] == '<':
            b.append(a[i])
            c += 1
        else:
            if len(b) == 0 or b[-1] != '<':
                break
            else:
                b.pop()
                if len(b) == 0:
                    ans += 2 * c
                    c = 0
    print(ans)
    t -= 1
