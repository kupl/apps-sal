def rev(s):
    s1 = ''
    for i in s:
        if(i == '0'):
            s1 = s1 + '1'
        else:
            s1 = s1 + '0'
    return s1


s = input()
s1 = ''
c = 0
for i in range(len(s) - 1, -1, -1):
    if(s[i] == '1'):
        s1 = rev(s[:i])
        c = c + 1
        s = s1

print(c)
