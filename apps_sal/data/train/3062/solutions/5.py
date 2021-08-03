def palindrome(num):
    if type(num) == int and num > 0:
        return str(num) == str(num)[::-1]
    else:
        return 'Not valid'

    # or, as an ugly one line - just for practice:

    # return str(num) == str(num)[::-1] if type(num) == int and num > 0 else 'Not valid'
