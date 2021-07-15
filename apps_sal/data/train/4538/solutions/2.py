def reverse_fun(n):
    n = n[::-1]
    for i in range(1, len(n)):
        n = n[:i] + n[i:][::-1]
    return n
