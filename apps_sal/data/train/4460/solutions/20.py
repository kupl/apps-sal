def whatday(n):
    if n<1 or n>7: return 'Wrong, please enter a number between 1 and 7'
    return ' Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split(' ')[n]

