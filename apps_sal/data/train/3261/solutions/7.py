def sort_poker(john, uncle):
    suits = ('S', 'D', 'H', 'C')
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def get_value(index, hand):
        return hand[index + 1:index + 3] if hand[index + 1] == '1' else hand[index + 1]

    def get_all_indexes(suit, hand):
        return [i for i in range(len(hand)) if hand.startswith(suit, i)]

    def get_cards(hand):
        return {suit: [get_value(index, hand) for index in get_all_indexes(suit, hand)] for suit in suits}

    def get_suit_rating(hand):
        return list(dict.fromkeys((symbol for symbol in hand if symbol in suits)))
    johns_hand = sorted([(suit, sorted([card for card in value], key=lambda x: values.index(x))) for (suit, value) in list(get_cards(john).items())], key=lambda x: get_suit_rating(uncle).index(x[0]))
    return ''.join((''.join((suit[0] + value for value in suit[1])) for suit in johns_hand))
