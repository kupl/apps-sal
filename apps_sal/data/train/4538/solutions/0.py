def reverse_fun(n):
    for i in range(len(n)):
        n = n[:i] + n[i:][::-1]
    return n
