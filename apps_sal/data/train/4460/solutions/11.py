def whatday(num):
    l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if 0 < num <= 7:
        for i in range(1, 8):
            if i == num:
                return l[i - 1]
    else:
        return 'Wrong, please enter a number between 1 and 7'
