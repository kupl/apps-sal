def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    steps = 0
    while True:
        reverse_n = int(str(n)[::-1])
        if n == reverse_n:
            return steps
            break
        else:
            n += reverse_n
            steps += 1
