def palindrome_chain_length(n):
    level = 0
    while n != int(str(n)[::-1]):
        n += int(str(n)[::-1])
        level += 1
    return level
