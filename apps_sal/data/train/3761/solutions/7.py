from collections import Counter


def strange_coach(players):
    first_letters = (player[0] for player in players)
    counts = Counter(first_letters)
    at_least_five = ''.join(sorted((k for (k, v) in counts.items() if v > 4)))
    return at_least_five or 'forfeit'
