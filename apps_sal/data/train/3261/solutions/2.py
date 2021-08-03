def order(arr): return {card[0]: i for i, card in enumerate(arr)}


ranks = order("2 3 4 5 6 7 8 9 10 J Q K A".split())
suit_table = {ord(suit): ' ' + suit for suit in 'SDHC'}
def split_hand(hand): return hand.translate(suit_table).split()


def sort_poker(john, uncle):
    suits = order(split_hand(uncle))
    return ''.join(sorted(split_hand(john),
                   key=lambda card: (suits[card[0]], ranks[card[1]])))
