t = int(input())
while t:
    s = input()
    while 'abc' in s:
        s = s.replace('abc', '')
    print(s)
    t -= 1
