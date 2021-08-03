
s = input()
x = len(s)

if set(s) == {'1'}:
    print(int(s[0:x - 1]))
else:
    for i in range(len(s)):
        if s[i] != '0':
            continue
        else:
            s = s[0:i] + s[i + 1:len(s)]
            print(int(s))
            break
