def palindrome(num):

    def helper():
        if type(num) == str or num < 0:
            return 'Not valid'
        return True if str(num) == str(num)[::-1] else False
    try:
        int(num)
    except ValueError:
        return 'Not valid'
    else:
        return helper()
