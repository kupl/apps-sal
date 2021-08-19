class PokerHand:

    def __init__(self, hand):
        hand = hand.split()
        values = sorted(('__23456789TJQKA'.index(card[0]) for card in hand))[::-1]
        same_suit = len({card[1] for card in hand}) == 1
        straight = [values[0] - i for i in range(5)] == values
        kinds = {i: [] for i in range(1, 5)}
        for value in sorted(set(values))[::-1]:
            how_many = values.count(value)
            kinds[how_many].append(value)
        if same_suit and straight:
            self.rank = (8, values)
        elif kinds[4]:
            self.rank = (7, kinds[4], kinds[1])
        elif kinds[3] and kinds[2]:
            self.rank = (6, kinds[3], kinds[2])
        elif same_suit:
            self.rank = (5, values)
        elif straight:
            self.rank = (4, values)
        elif kinds[3]:
            self.rank = (3, kinds[3], kinds[1])
        elif len(kinds[2]) == 2:
            self.rank = (2, kinds[2], kinds[1])
        elif kinds[2]:
            self.rank = (1, kinds[2], kinds[1])
        else:
            self.rank = (0, values)

    def compare_with(self, other):
        return 'Win' if self.rank > other.rank else 'Loss' if self.rank < other.rank else 'Tie'
