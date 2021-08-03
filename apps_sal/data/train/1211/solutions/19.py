for _ in range(int(input())):
    s = input()
    x = 'abc'
    while x in s:
        s = s.replace('abc', '')
    print(s)
