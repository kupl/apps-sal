def palindrome_chain_length(n):
    c = 0
    if str(n) != str(n)[::-1]:
        while str(n) != str(n)[::-1]:
            n += int(str(n)[::-1])
            c += 1
        return c
    else:
        return 0
