def palindrome_chain_length(n):
    steps = 0
    value = str(n)
    while value != value[::-1]:
        value = str(int(value) + int(value[::-1]))
        steps += 1
    return steps
