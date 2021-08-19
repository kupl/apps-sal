t = int(input())
while t > 0:
    s = input()
    i = fl = 0
    while i < len(s):
        if s[i] == s[i + 1]:
            fl = 1
            break
        i += 2
    if fl == 0:
        print('yes')
    elif fl == 1:
        print('no')
    t -= 1
