m = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}


def check_challenge(pledged, current, month):
    t = [pledged // 12] * 12
    for i in range(pledged % 12):
        t[i] += 1
    x = sum(t[:m[month] - 1])
    if month == 'January' or current == x:
        return 'You are on track.'
    elif pledged <= current:
        return 'Challenge is completed.'
    elif current < x:
        return 'You are {} behind schedule.'.format(x - current)
    else:
        return 'You are {} ahead of schedule!'.format(current - x)
