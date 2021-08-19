def whatday(num):
    return (['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][num - 1:num] + ['Wrong, please enter a number between 1 and 7'])[0]
