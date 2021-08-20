def palindrome_chain_length(n):
    step = 0
    while str(n)[:] != str(n)[::-1]:
        n += int(str(n)[::-1])
        step += 1
    return step
