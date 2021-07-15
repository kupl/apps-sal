def palindrome(num):
    return 'Not valid' if type(num) is not int or num < 0 else str(num) == str(num)[::-1]
