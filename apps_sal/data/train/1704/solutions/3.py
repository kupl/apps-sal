from collections import Counter

RESULT = ["Loss", "Tie", "Win"]
HEX_CARDS = "23456789ABCDE"
CARD_TO_HEX = str.maketrans("TJQKA", "ABCDE")
MAIN_RANK = [lambda colC, valC, isS: 5 in colC.values() and isS,                    # Straight Flush
             lambda colC, valC, isS: 4 in valC.values(),                            # Square
             lambda colC, valC, isS: 3 in valC.values() and 2 in valC.values(),     # Full house
             lambda colC, valC, isS: 5 in colC.values(),                            # Flush
             lambda colC, valC, isS: isS,                                           # Straight
             lambda colC, valC, isS: 3 in valC.values(),                            # Three of a kind
             lambda colC, valC, isS: 2 in valC.values() and len(valC.keys()) == 3,  # 2 pairs
             lambda colC, valC, isS: 2 in valC.values() and len(valC.keys()) == 4,  # 1 pair,
             lambda colC, valC, isS: True]                                          # 1 card


class PokerHand(object):

    def __init__(self, hand):
        hand = hand.translate(CARD_TO_HEX)
        valCount = Counter(hand[n] for n in range(0, len(hand), 3))
        colorCount = Counter(hand[n] for n in range(1, len(hand), 3))

        minCardIdx = int(min(valCount.keys()), 16) - 2
        isStraight = valCount.keys() == set(HEX_CARDS[minCardIdx:minCardIdx + 5])
        hashSameRank = int(''.join(sorted(valCount.keys(), key=lambda k: (valCount[k], k), reverse=True)), 16)

        for i, func in enumerate(MAIN_RANK):
            if func(colorCount, valCount, isStraight):
                self.handValue = (len(MAIN_RANK) - i) * 16**5 + hashSameRank
                break

    def compare_with(self, other):
        return RESULT[(self.handValue >= other.handValue) + (self.handValue > other.handValue)]
