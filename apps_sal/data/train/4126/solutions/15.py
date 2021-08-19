def what_time_is_it(angle):
    minutes = int(angle * 2)
    hours = minutes // 60 or 12
    minutes %= 60
    return f'{hours:02}:{minutes:02}'
