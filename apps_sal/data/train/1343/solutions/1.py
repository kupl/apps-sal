t = int(input())
for _ in range(t):
    s = input()
    if len(s) % 2 == 0:
        ok = True
        for i in range(len(s) // 2):
            if s[i] != s[i + len(s) // 2]:
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')
    elif len(s) == 1:
        print('NO')
    else:
        idx1 = 0
        idx2 = len(s) // 2
        ok = False
        while idx1 < len(s) // 2 and idx2 < len(s):
            if s[idx1] != s[idx2]:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
        if idx1 == len(s) // 2:
            ok = ok or True
        idx1 = len(s) // 2 + 1
        idx2 = 0
        while idx1 < len(s) and idx2 <= len(s) // 2:
            if s[idx1] != s[idx2]:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
        if idx1 == len(s):
            ok = ok or True
        if ok:
            print('YES')
        else:
            print('NO')
