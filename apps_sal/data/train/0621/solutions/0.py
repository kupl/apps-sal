t = eval(input())
for _ in range(t):
    n = eval(input())
    a = input().strip().split()
    cb, cs = 0, ""
    for i in range(len(a[0])):
        for j in range(i + 1, len(a[0]) + 1):
            al = True
            s = a[0][i:j]
            for k in a[1:]:
                if s not in k:
                    al = False
                    break
            if al:
                if j - i >= cb:
                    cb = max(cb, j - i)
                    if len(cs) < cb:
                        cs = a[0][i:j]
                    elif len(cs) == cb:
                        cs = min(cs, a[0][i:j])
    print(cs)
