
s = list(input())

f = False
c = False

for i in range(len(s)):
    ss = s[i]
    if ss == 'a':
        if f is True:
            print(''.join(s))
            return
        else:
            continue
    else:
        s[i] = chr(ord(ss) - 1)
        f = True
        c = True

if c is False:
    s[-1] = 'z'

print(''.join(s))
