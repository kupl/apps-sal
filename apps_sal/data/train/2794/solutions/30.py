def calculate_age(yob, cy):
    if cy == yob + 1:
        return 'You are 1 year old.'
    if yob == cy + 1:
        return 'You will be born in 1 year.'
    return 'You were born this very year!' if yob == cy else f'You are {cy - yob} years old.' if cy > yob else f'You will be born in {yob - cy} years.'
