def card_game(card_1, card_2, trump):
    card_1_wins, card_2_wins, cards = "The first card won.", "The second card won.", {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if card_1 == card_2:
        return "Someone cheats."
    if card_1 == "joker":
        return card_1_wins
    if card_2 == "joker":
        return card_2_wins
    if card_1[-1] == card_2[-1]:
        card_1_value = cards[card_1[0:-1]] if card_1[0:-1].isalpha() else int(card_1[0:-1])
        card_2_value = cards[card_2[0:-1]] if card_2[0:-1].isalpha() else int(card_2[0:-1])
        return card_1_wins if card_1_value > card_2_value else card_2_wins
    return card_1_wins if card_1[-1] == trump else card_2_wins if card_2[-1] == trump else "Let us play again."
