# cook your dish here
try:
    for t in range(int(input())):
        n = input()
        m = list(n)
        for i, j in enumerate(m):
            m[i] = str(int(j) - 2)
        print(''.join(m))
except EOFError:
    pass
