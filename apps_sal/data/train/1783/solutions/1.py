from collections import Counter
HEX_CARDS = '23456789ABCDE'
CARD_TO_HEX = str.maketrans('TJQKA', 'ABCDE')


class PokerHand(object):

    def __init__(self, hand):
        self.hand = hand
        hand = hand.translate(CARD_TO_HEX)
        valCount = Counter((hand[n] for n in range(0, len(hand), 3)))
        colorCount = Counter((hand[n] for n in range(1, len(hand), 3)))
        minCardIdx = int(min(valCount.keys()), 16) - 2
        isStraight = list(valCount.keys()) == set(HEX_CARDS[minCardIdx:minCardIdx + 5])
        if list(valCount.keys()) == {'2', '3', '4', '5', 'E'}:
            isStraight = True
            valCount['1'] = valCount.pop('E')
        mainVal = next((i for (i, elt) in enumerate([5 in list(colorCount.values()) and isStraight, 4 in list(valCount.values()), 3 in list(valCount.values()) and 2 in list(valCount.values()), 5 in list(colorCount.values()), isStraight, 3 in list(valCount.values()), 2 in list(valCount.values()) and len(list(valCount.keys())) == 3, 2 in list(valCount.values()) and len(list(valCount.keys())) == 4, True]) if elt))
        self.handValue = int(''.join(sorted(list(valCount.keys()), key=lambda k: (valCount[k], k), reverse=True)), 16) + (8 - mainVal) * 16 ** 5

    def __eq__(self, other):
        return self.handValue == other.handValue

    def __lt__(self, other):
        return self.handValue > other.handValue

    def __gt__(self, other):
        return self.handValue < other.handValue

    def __repr__(self):
        return 'PokerHand({})'.format(self.hand)
