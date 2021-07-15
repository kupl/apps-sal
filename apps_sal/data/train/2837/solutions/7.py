def what_is_the_time(time):
    a,b = map(int,time.split(':'))
    if 1<=a<=10 and 1<=b<=59 : a, b = 11-a, 60-b
    elif 11<=a<=12 and 1<=b<=59 : a, b = 23-a,60-b
    else : a, b = 12-a,b
    return '{0:>02}:{1:>02}'.format(a or 12,b)
