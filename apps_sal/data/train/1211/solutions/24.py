# cook your dish here

t = int(input())

while t:
    s = input()

    while 'abc' in s:
        s = s.replace('abc', '')
        # print(s)

    print(s)

    t -= 1
