def add_binary(a, b):
    # your code here
    c = a + b
    x = ''
    while(c != 0):
        z = c % 2
        x += str(z)
        c = c // 2
    return x[::-1]
