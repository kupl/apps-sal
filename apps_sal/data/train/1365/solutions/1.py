from itertools import combinations as cb
s = input()
s = list(s)
if 'c' in s or 'k' in s:
    print('0')
else:
    nf = []
    nk = []
    i = 0
    while i < len(s) - 1:
        if s[i] == 'f':
            j = i + 1
            p = 1
            k = 1
            while j < len(s) and p:
                if s[j] == 'f':
                    k += 1
                    j += 1
                else:
                    p = 0
            nf.append(k)
            i = j
        elif s[i] == 'g':
            j = i + 1
            p = 1
            k = 1
            while j < len(s) and p:
                if s[j] == 'g':
                    k += 1
                    j += 1
                else:
                    p = 0
            nk.append(k)
            i = j
        else:
            i += 1
    p = 1
    for i in nf:
        n = i
        if n >= 2:
            k = 0
            for j in range(1, n + 1):
                a = n // j - 1
                k += a
            k += 1
            p *= k
    for i in nk:
        n = i
        if n >= 2:
            k = 0
            for j in range(1, n + 1):
                a = n // j - 1
                k += a
            k += 1
            p *= k
    if nf != [] and nk != []:
        if len(s) == nf[0] or len(s) == nk[0]:
            count = p - 1
        else:
            count = p
    elif nf == [] and nk != []:
        if len(s) == nk[0]:
            count = p - 1
        else:
            count = p
    elif nf != [] and nk == []:
        if len(s) == nf[0]:
            count = p - 1
        else:
            count = p
    else:
        count = 1
    print(count % 1000000007)
