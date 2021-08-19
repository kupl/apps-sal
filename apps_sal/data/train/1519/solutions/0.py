# cook your dish here
for _ in range(int(input(''))):
    n = int(input(''))
    x = bin(n)
    x = len(x) - 2
    if n == (2**(x - 1)):
        print(n)
    else:
        print(2**x)
