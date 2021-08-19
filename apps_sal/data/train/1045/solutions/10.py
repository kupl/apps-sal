test = int(input())
for _ in range(test):
    s = input()
    a = ''
    for i in s:
        if i != '\r':
            if i in ['a', 'e', 'i', 'o', 'u']:
                a += '0'
            else:
                a += '1'
    ans = int(a, 2)
    print(ans % (1000000000 + 7))
