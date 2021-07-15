def whatday(num):
    dict ={1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 0: 'Sunday'}
    return dict.get(num-1, 'Wrong, please enter a number between 1 and 7')
