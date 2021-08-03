ranks = "23456789TJQKA"


def winner(deck_steve, deck_josh):
    steve_points = sum([1 for i in range(len(deck_steve)) if ranks.index(deck_steve[i]) > ranks.index(deck_josh[i])])
    josh_points = sum([1 for i in range(len(deck_josh)) if ranks.index(deck_steve[i]) < ranks.index(deck_josh[i])])
    if steve_points > josh_points:
        return "Steve wins %d to %d" % (steve_points, josh_points)
    elif josh_points > steve_points:
        return "Josh wins %d to %d" % (josh_points, steve_points)
    else:
        return "Tie"
