def boredom(staff):
    depts = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
    b = sum((depts[v] for v in staff.values()))
    return 'kill me now' if b <= 80 else 'i can handle this' if b < 100 else 'party time!!'
