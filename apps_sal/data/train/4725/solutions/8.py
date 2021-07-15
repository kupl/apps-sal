def reverse(n, acc = 0):
    return acc if n == 0 else reverse(n//10, acc*10 + n%10)
