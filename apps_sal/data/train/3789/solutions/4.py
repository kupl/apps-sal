def score_throws(radii):
    if not radii:
        return 0
    sum = 0
    for i in radii:
        if i >= 5 and i <= 10:
            sum += 5
        elif i < 5:
            sum += 10
    return sum + 100 if max(radii) < 5 else sum
