def whatday(num):
    days = {2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday', 1: 'Sunday'}
    try:
        return days[num]
    except:
        return 'Wrong, please enter a number between 1 and 7'
