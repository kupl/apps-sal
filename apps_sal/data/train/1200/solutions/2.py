t = int(input())
for _ in range(t):
    s = input()
    c = 0
    for i in range(0, len(s) - 1, 2):
        if s[i] == 'B' and s[i + 1] == 'A' or (s[i] == 'A' and s[i + 1] == 'B'):
            pass
        else:
            c = 1
            break
    if c == 1:
        print('no')
    else:
        print('yes')
