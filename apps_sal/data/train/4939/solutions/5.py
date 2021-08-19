def coffee_limits(year, month, day):
    health_no = int('{:04}{:02}{:02}'.format(year, month, day))
    (cafe, decaf) = (health_no, health_no)
    cups = 0
    for i in range(5000):
        cafe += 51966
        cups += 1
        if 'DEAD' in '{:08X}'.format(cafe):
            break
    cafe = 0 if cups == 5000 else cups
    cups = 0
    for i in range(5000):
        decaf += 912559
        cups += 1
        if 'DEAD' in '{:08X}'.format(decaf):
            break
    decaf = 0 if cups == 5000 else cups
    return [cafe, decaf]
