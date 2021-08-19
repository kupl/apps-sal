f = 0
t = int(input())
while t > 0:
    t -= 1
    o = 0
    s = input()
    s = list(s)
    n = len(s)
    if len(s) == 1:
        print('NO')
        continue
    if len(s) % 2 == 1:
        for i in range(n):
            ls = s.copy()
            ls.pop(i)
            if ls[0:int(len(ls) / 2)] == ls[int(len(ls) / 2):int(len(ls))]:
                print('YES')
                o = 1
                break
        if o == 0:
            print('NO')
    elif s[0:int(len(s) / 2)] == s[int(len(s) / 2):int(len(s))]:
        print('YES')
    else:
        print('NO')
