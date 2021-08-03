def points(games):
    count = 0
    for i in games:
        a, b = i.split(':')
        if a > b:
            count += 3
        elif a == b:
            count += 1
        else:
            continue

    return count
