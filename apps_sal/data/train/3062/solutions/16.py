def palindrome(num):
    if isinstance(num, int) is False or num < 0:
        return 'Not valid'
    return str(num) == str(num)[::-1]
