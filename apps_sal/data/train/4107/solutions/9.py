from datetime import date, datetime


def half_life(person1, person2):
    d0, d1 = sorted([
        datetime.strptime(person1, '%Y-%m-%d').date(),
        datetime.strptime(person2, '%Y-%m-%d').date()
    ])
    return (d1 + (d1 - d0)).isoformat()
