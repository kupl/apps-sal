def palindrome_chain_length(n):
    steps = 0
    if str(n) == str(n)[::-1]:
        return steps
    else:
        while str(n) != str(n)[::-1]:
            n += int(str(n)[::-1])
            steps += 1
    return steps
