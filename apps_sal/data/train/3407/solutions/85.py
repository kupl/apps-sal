def palindrome_chain_length(n):
    def reverse(x):
        return int(str(x)[::-1])
        
    def is_palindrome(x):
        return x == reverse(x)
        
    steps = 0
    while not is_palindrome(n):
        n += reverse(n)
        steps += 1

    # parameter n is a positive integer
    # your function should return the number of steps
    return steps
