n = int(input())
l = []
for i in range(0, n):
    s = input()
    for j in range(0, len(s), 2):
        if s[j] == 'A' and s[j + 1] == 'B' or (s[j] == 'B' and s[j + 1] == 'A'):
            count = 1
        else:
            l.append('no')
            count = 0
            break
    if count == 1:
        l.append('yes')
for i in l:
    print(i)
