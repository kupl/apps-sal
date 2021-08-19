def palindrome_chain_length(n):
    count = 0
    while int(str(n)[::-1]) != n:
        n = n + int(str(n)[::-1])
        count += 1
    return count
