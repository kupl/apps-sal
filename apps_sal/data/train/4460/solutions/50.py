import calendar

def whatday(num):
    ll = ['Sunday'] + list(calendar.day_name)[:-1]
    print(num, ll)
    return ll[num - 1] if num in range(1, 8) else 'Wrong, please enter a number between 1 and 7'
