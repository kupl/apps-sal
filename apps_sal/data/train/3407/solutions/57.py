def palindrome_chain_length(n):
    x = n
    i = 0
    while str(x) != str(x)[::-1]:
        x = x + int(str(x)[::-1])
        i = i + 1
    return i
