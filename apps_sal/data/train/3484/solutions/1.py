def time_convert(num):
    if num <= 0:
        return '00:00'
    return f'{num//60:02}:{num%60:02}'
