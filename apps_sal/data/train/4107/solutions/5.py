from datetime import datetime


def half_life(person1, person2):
    (person1, person2) = sorted((person1, person2))
    p1 = datetime.strptime(person1, '%Y-%m-%d')
    p2 = datetime.strptime(person2, '%Y-%m-%d')
    return (p2 + (p2 - p1)).strftime('%Y-%m-%d')
