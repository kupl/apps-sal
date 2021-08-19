def palindrome(num):
    if isinstance(num, int) == False or num < 0:
        return 'Not valid'
    elif str(num) == str(num)[::-1]:
        return True
    else:
        return False
