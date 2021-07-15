def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    n_str = str(n)
    steps = 0
    
    while n_str != n_str[::-1]:
        steps += 1
        palindrome = int(n_str) + int(n_str[::-1])
        n_str = str(palindrome)
        
    return steps
