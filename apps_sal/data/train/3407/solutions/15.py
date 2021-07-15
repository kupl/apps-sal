def palindrome_chain_length(n):
    ct = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        ct += 1
    return ct
