scores = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}


def boredom(staff):
    score = sum((scores[activity] for activity in staff.values()))
    return 'party time!!' if score >= 100 else 'i can handle this' if score > 80 else 'kill me now'
