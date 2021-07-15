def palindrome_chain_length(n):
    steps = 0
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        steps += 1
    return steps
