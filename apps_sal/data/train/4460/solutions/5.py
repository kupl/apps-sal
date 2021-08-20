def whatday(n):
    return 'Wrong, please enter a number between 1 and 7' * (n > 7 or n < 1) or __import__('calendar').day_name[n - 2]
