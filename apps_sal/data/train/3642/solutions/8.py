def boredom(staff):
    D = {'accounts': 1,
         'finance': 2,
         'canteen': 10,
         'regulation': 3,
         'trading': 6,
         'change': 6,
         'IS': 8,
         'retail': 5,
         'cleaning': 4,
         'pissing about': 25,
         }
    score = sum([D[key] for key in list(staff.values())])
    if score <= 80:
        ans = 'kill me now'
    elif 80 < score < 100:
        ans = 'i can handle this'
    elif score >= 100:
        ans = 'party time!!'
    return ans
