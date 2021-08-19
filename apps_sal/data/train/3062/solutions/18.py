def palindrome(num):
    if isinstance(num, int) and num >= 0:
        num = str(num)
        return num == num[::-1]
    else:
        return 'Not valid'
