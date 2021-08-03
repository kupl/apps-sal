t = eval(input())
while t:
    m = 101
    n = eval(input())
    while n:
        s = input()
        a = s.count('a')
        b = s.count('b')
        m = min(a, b, m)
        n -= 1
    print(m)
    t -= 1
