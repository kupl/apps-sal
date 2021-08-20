t = int(input())
for x in range(t):
    ss = ''
    s = input()
    for i in s:
        if i in 'aeiou':
            ss = ss + '1'
        else:
            ss = ss + '0'
    l = len(ss)
    res = 0
    for i in range(l):
        res = res + int(ss[i]) * (2 ** (l - 1 - i) % 1000000007) % 1000000007
    print(res)
