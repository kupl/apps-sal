def palindrome_chain_length(n):
    steps = 0
    while True:
        n_str = str(n)
        if n_str == n_str[::-1]:
            return steps
        else:
            n += int(n_str[::-1])
            steps += 1
