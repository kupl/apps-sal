t = int(input())
for _ in range(t):
    n = input()
    s = 0
    p = 0
    h = 0
    if(len(n) == 1):
        if(n[0] == '.'):
            print(1)
        else:
            print(0)
    else:
        for i in range(len(n) - 1):
            if(n[i] == '.'):
                p += 1
                if(n[i + 1] == '
                    if(p > s):
                        h += 1
                        s=p
                    p=0
        if(h == 0 and n[len(n) - 1] == '.'):
            print(1)
        else:
            print(h)
