value = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
def get_val(x): return value[x] if x in value else int(x)


def card_game(card_1, card_2, trump):
    if card_1 == card_2:
        return "Someone cheats."
    if card_1 == "joker":
        return "The first card won."
    if card_2 == "joker":
        return "The second card won."
    if card_1[-1] == card_2[-1]:
        return "The first card won." if get_val(card_1[:-1]) > get_val(card_2[:-1]) else "The second card won."
    if card_1[-1] == trump:
        return "The first card won."
    if card_2[-1] == trump:
        return "The second card won."
    return "Let us play again."
