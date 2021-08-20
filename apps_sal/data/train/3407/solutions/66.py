def palindrome_chain_length(n):
    n1 = str(n)
    n1 = n1[::-1]
    n1 = int(n1)
    x = 0
    while n != n1:
        n += n1
        n1 = str(n)
        n1 = n1[::-1]
        n1 = int(n1)
        x += 1
    return x
