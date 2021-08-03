def unbalancing(s):
    x = 0
    retvalue = 0
    for c in s:
        if c == '(':
            x += 1
        else:
            x -= 1
        retvalue = min(retvalue, x)
    return retvalue


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(-unbalancing(s))
