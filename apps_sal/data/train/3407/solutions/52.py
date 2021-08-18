def palindrome_chain_length(n):
    count = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        count += 1

    return count
