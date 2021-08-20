t = int(input())
while t:
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    n = int(input())
    s = input()
    res = ''
    for i in range(0, len(s), 4):
        res = res + a[int(s[i:i + 4], 2)]
    print(res)
    t -= 1
