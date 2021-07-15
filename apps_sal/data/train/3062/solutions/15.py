def palindrome(num):
    return str(num) == str(num)[::-1] if type(num) is int and num >= 0 else 'Not valid'
