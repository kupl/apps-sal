def palindrome(num):
    return str(num)[::-1] == str(num) if isinstance(num, int) and num > 0 else 'Not valid'
