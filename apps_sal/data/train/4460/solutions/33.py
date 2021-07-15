wd = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def whatday(num):
    if num < 1 or num > 7:
        return 'Wrong, please enter a number between 1 and 7'
    return wd[num - 1]

