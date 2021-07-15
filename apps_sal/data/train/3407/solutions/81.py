def IsPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def palindrome_chain_length(n):
    result = 0
    # parameter n is a positive integer
    # your function should return the number of steps
    while not IsPalindrome(n):
        n = n + int(str(n)[::-1])
        result += 1

    return result
