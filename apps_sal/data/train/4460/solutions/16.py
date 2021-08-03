def whatday(num):
    return dict(zip('2345671', __import__('calendar').day_name)).get(str(num), 'Wrong, please enter a number between 1 and 7')
