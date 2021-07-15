ranks = "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"


def cmp(a, b):
    return (a > b) - (b > a)


def winner(deck_steve, deck_josh):
    points = [0, 0, 0]
    for xs in zip(deck_steve, deck_josh):
        s, j = map(ranks.index, xs)
        points[0 if s > j else 1 if s < j else 2] += 1
    if points[0] > points[1]:
        return f"Steve wins {points[0]} to {points[1]}"
    elif points[1] > points[0]:
        return f"Josh wins {points[1]} to {points[0]}"
    else:
        return "Tie"
