t = int(input())
while t:
    t -= 1
    l = int(input())
    s = list(input())
    l = []
    a = 0
    for i in range(len(s)):
        if s[i] != '.':
            l.append(s[i])
    for i in range(0, len(l) - 1, 2):
        if l[i] == 'H' and l[i + 1] == 'T':
            a += 2
    if a == len(l):
        print('Valid')
    else:
        print('Invalid')
