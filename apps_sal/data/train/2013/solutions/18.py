s = list(input())
a = 0
if set(s) == {'a'}:
    s[-1] = '{'
for i in range(len(s)):
    if a == 0:
        if s[i] == 'a':
            continue
        else:
            s[i] = chr(ord(s[i]) - 1)
            a = 1
    else:
        if s[i] == 'a':
            break
        else:
            s[i] = chr(ord(s[i]) - 1)
print(''.join(s))
