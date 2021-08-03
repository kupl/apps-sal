def palindrome_chain_length(n):
    counter = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        counter += 1
    if counter > 0:
        return counter
    return 0
