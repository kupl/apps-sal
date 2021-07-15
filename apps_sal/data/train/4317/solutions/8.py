def card_game(card_1, card_2, trump):
    deck_dict = {'J':11, 'Q':12, 'K':13, 'A':14}
    suit_1 = card_1[-1]
    suit_2 = card_2[-1]
    if card_1 == card_2: return 'Someone cheats.'
    elif card_1 == 'joker': return 'The first card won.'
    elif card_2 == 'joker': return 'The second card won.'
    rank_1 = card_1[0:-1]
    rank_2 = card_2[0:-1]
    rank_1 = int(deck_dict.get(rank_1,rank_1))
    rank_2 = int(deck_dict.get(rank_2,rank_2))

    if   suit_1 == suit_2 and rank_1 > rank_2: return 'The first card won.'
    elif suit_1 == suit_2 and rank_1 < rank_2: return 'The second card won.'

    elif suit_1 != suit_2 and suit_1 != trump and suit_2 != trump: return 'Let us play again.'

    elif suit_1 == trump: return 'The first card won.'
    elif suit_2 == trump: return 'The second card won.'

    return 'Oops'

