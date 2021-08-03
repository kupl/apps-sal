def fizz_buzz_cuckoo_clock(time):
    hour, min = [int(x) for x in time.split(':')]

    hour = hour % 12
    hour = 12 if hour == 0 else hour

    if min == 0:
        return ' '.join(hour * ['Cuckoo'])
    elif min == 30:
        return 'Cuckoo'
    elif min % 15 == 0:
        return 'Fizz Buzz'
    elif min % 5 == 0:
        return 'Buzz'
    elif min % 3 == 0:
        return 'Fizz'
    else:
        return 'tick'
