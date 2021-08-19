for u in range(int(input())):
    s = input()
    n = len(s)
    x = s.count('a')
    z = n - x
    s = 2 ** x - 1
    c = 2 ** z
    print(s * c)
