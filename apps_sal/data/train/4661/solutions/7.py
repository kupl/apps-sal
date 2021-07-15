def pattern(n):
    digits = ''.join([str(i % 10) for i in range(1,n+1)])
    return '\n'.join([' ' * (n - 1 -i) + digits + ' ' * i for i in range(n)])
