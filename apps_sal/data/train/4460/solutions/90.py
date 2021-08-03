def whatday(num):
    if num in [1, 2, 3, 4, 5, 6, 7]:
        return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][num - 1]
    else:
        return 'Wrong, please enter a number between 1 and 7'
