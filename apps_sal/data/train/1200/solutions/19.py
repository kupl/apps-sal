t = int(input())
for j in range(t):
    s = input()
    a = 0
    for i in range(0, len(s) - 1, 2):
        if s[i] == 'A' and s[i + 1] == 'B' or (s[i] == 'B' and s[i + 1] == 'A'):
            a = a + 1
    if a == len(s) / 2:
        print('yes')
    else:
        print('no')
