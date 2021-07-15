def tickets(people):
    change = {
        '25': 0,
        '50': 0
    }
    for person in people:
        if person == 25:
            change['25'] += 1
        elif person == 50:
            change['50'] += 1
            change['25'] -= 1
        else:
            if change['50'] > 0:
                change['50'] -= 1
                change['25'] -= 1
            else:
                change['25'] -= 3
        if change['25'] < 0:
            return 'NO'
    return 'YES'
