# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    c = 0
    for i in range(len(s)):
        if s[i] == '.':
            continue
        if s[i] == 'H':
            c += 1
        if s[i] == 'T':
            c -= 1
        if c > 1:
            break
        if c < 0:
            break
    if c == 0:
        print('Valid')
    else:
        print('Invalid')
