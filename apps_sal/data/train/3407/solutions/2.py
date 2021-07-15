def is_palindrome(n):
    return str(n) == str(n)[::-1]
    

def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    steps = 0
    while not is_palindrome(n):
        steps += 1
        n += int(str(n)[::-1])
    return steps

