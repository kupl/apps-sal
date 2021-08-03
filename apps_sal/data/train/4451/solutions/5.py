def digitsum(x):
    total = 0
    for letter in str(x):
        total += ord(letter) - 48
    return total


def golf_score_calculator(par, score):
    return digitsum(score) - digitsum(par)
