def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    i = 0
    while True:
        if n == int(str(n)[::-1]):          
            return i
        n += int(str(n)[::-1])
        i += 1
