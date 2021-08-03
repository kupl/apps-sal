def palindrome_chain_length(n):
    count = 0
    while int(str(n)[::-1]) != n:
        count += 1
        n += int(str(n)[::-1])
    return count
