CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDS_VAL = {elt: i for i, elt in enumerate(CARDS)}


def winner(deck_steve, deck_josh):
    resultLst = [CARDS_VAL[c1] > CARDS_VAL[c2] for c1, c2 in zip(deck_steve, deck_josh) if CARDS_VAL[c1] != CARDS_VAL[c2]]
    result, l = sum(resultLst), len(resultLst)
    return ["Josh wins {} to {}".format(l - result, result),
            "Steve wins {} to {}".format(result, l - result),
            "Tie"][(result >= l / 2.0) + (result == l / 2.0)]
