def palindrome_chain_length(n):
    i = 0
    while True:
        if n == int(str(n)[::-1]):
            return i
        n += int(str(n)[::-1])
        i += 1
