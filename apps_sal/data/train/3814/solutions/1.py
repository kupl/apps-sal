def get_military_time(time_str):
    hour = int(time_str[:2])
    pm = time_str[-2] == 'P'
    return f'{hour % 12 + 12 * pm:02}{time_str[2:-2]}'
