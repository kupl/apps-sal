def palindrome_chain_length(n):
    loop = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        loop += 1
    return loop
