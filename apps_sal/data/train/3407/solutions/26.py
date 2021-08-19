def palindrome_chain_length(n):

    def digits_reversed(n):
        return int(str(n)[::-1])
    steps = 0
    last_n = n
    last_n_rev = digits_reversed(last_n)
    while last_n != last_n_rev:
        last_n += last_n_rev
        last_n_rev = digits_reversed(last_n)
        steps += 1
    return steps
