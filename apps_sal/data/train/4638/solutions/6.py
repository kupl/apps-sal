def fizz_buzz_cuckoo_clock(time):
    m=int(time[3:])
    h=int(time[:2])
    if m==0:
        return ('Cuckoo '*(h%12 or 12))[:-1]
    elif m==30:
        return 'Cuckoo'
    else:
        if m%3==0:
            if m%5==0:
                return 'Fizz Buzz'
            else:
                return 'Fizz'
        elif m%5==0:
            return 'Buzz'
        else:
            return 'tick'

