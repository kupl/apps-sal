from collections import Counter
from string import ascii_lowercase

def strange_coach(players):
    first_letters = Counter(player[0] for player in players)
    return "".join(c for c in ascii_lowercase if first_letters[c] >= 5) or "forfeit"
