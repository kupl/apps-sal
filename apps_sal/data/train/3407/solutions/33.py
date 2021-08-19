def palindrome_chain_length(n):
    (num, s) = (0, str(n))
    while s != s[::-1]:
        num += 1
        s = str(int(s) + int(s[::-1]))
    return num
