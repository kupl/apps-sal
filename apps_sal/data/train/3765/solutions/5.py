from collections import Counter

def highest_age(group1, group2):
    total = Counter()
    for person in group1 + group2:
        total[person['name']] += person['age']
    return min(total, key=lambda name: (-total[name], name))
