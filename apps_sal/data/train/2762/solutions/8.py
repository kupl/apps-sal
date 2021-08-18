def scoreboard(announcement):
    '''Return scores as numbers from announcement'''
    numbers = {
        'nil': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    scores = announcement.split()[-2:]
    return [numbers[score] for score in scores]
