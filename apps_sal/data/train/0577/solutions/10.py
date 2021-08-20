def correct_string(s):
    a = set(s)
    if len(a) == len(s):
        return 1
    return 0


s = input()
if correct_string(s):
    s = sorted(s)
    s1 = ''.join(s)
    n = int(input())
    if n >= 1 and n <= 1000:
        for x in range(0, n):
            v = input()
            v = set(v)
            lw = len(v)
            if lw >= 1 and lw <= 12:
                v = sorted(v)
                s2 = ''.join(v)
                if s1 == s2:
                    print('Yes')
                else:
                    print('No')
            pass
