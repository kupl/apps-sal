def boredom(staff):
    dict_ = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
    summ = sum((dict_[i] for i in staff.values()))
    return 'kill me now' if summ <= 80 else 'i can handle this' if 100 > summ > 80 else 'party time!!'
