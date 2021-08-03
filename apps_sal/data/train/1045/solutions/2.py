t = int(input())
for _ in range(t):
    s = input()
    l = ['a', 'e', 'i', 'o', 'u']
    x = ''
    for i in range(len(s)):
        if s[i] in l or s[i] == ' ':
            x += '0'
        else:
            if s[i].islower():
                x += '1'
    k = int(x, 2)
    print(k % 1000000007)
