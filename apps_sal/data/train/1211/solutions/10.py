t = int(input())
for i in range(t):
    s = input()
    while 'abc' in s:
        s = s.replace('abc', '')
    print(s)
