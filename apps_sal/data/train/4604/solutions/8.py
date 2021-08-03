def palindrome(n):
    if type(n) is not int or n < 0:
        return 'Not valid'
    patterns = [2 * str(i) for i in range(10)] + [str(i) + str(j) + str(i) for j in range(10) for i in range(10)]
    for p in patterns:
        if p in str(n):
            return True
    return False
