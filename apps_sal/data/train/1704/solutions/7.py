from collections import Counter


class PokerHand(object):

    def __init__(self, hand):
        self.hand = ''.join(hand.split())

    def evaluate(self):

        HIERARCHY = {'highcard': 1, 'pair': 2, 'two_pairs': 3, 'three_of_aKind': 4,
                     'straight': 5, 'flush': 6, 'full_house': 7, 'four_of_aKind': 8,
                     'straight_flush': 9, 'royal_flush': 10}

        PRECEDENCE = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        value = sorted(PRECEDENCE[x] for x in self.hand[::2])
        shape = self.hand[1::2]

        # royal flush
        if len(set(shape)) == 1 and value == [10, 11, 12, 13, 14]:
            return HIERARCHY['royal_flush'], value, 'royal_flush'

        # straight_flush
        elif len(set(shape)) == 1 and all(abs(value[i] - value[i + 1]) == 1 for i in range(len(value) - 1)):
            return HIERARCHY['straight_flush'], value, 'straight_flush'

        # four of a kind
        elif any(value.count(x) == 4 for x in set(value)):
            return HIERARCHY['four_of_aKind'], value, 'four_of_aKind'

        # full house
        elif any(value.count(x) == 3 for x in set(value)) \
                and                         \
                any(value.count(x) == 2 for x in set(value)):
            return HIERARCHY['full_house'], value, 'full_house'

        # flush
        elif len(set(shape)) == 1:
            return HIERARCHY['flush'], value, 'flush'

        # straight
        elif all(abs(value[i] - value[i + 1]) == 1 for i in range(len(value) - 1)):
            return HIERARCHY['straight'], value, 'straight'

        # three of a kind
        elif any(value.count(x) == 3 for x in set(value)):
            return HIERARCHY['three_of_aKind'], value, 'three_of_aKind'

        # two pairs
        elif Counter(value).most_common(2)[-1][-1] == 2:
            return HIERARCHY['two_pairs'], value, 'two_pairs'

        # pair
        elif any(value.count(x) == 2 for x in set(value)):
            return HIERARCHY['pair'], value, 'pair'

        # high Card
        else:
            return HIERARCHY['highcard'], value, 'highcard'

    def compare_with(self, other):
        rank, cards, combo = self.evaluate()
        other_rank, other_cards, other_combo = other.evaluate()

        if rank > other_rank:
            return 'Win'

        elif rank == other_rank:
            if cards == other_cards:
                return 'Tie'

            elif combo == 'straight_flush' or combo == 'straight':
                if cards.pop() > other_cards.pop():
                    return 'Win'
                else:
                    return 'Loss'

            elif combo == 'four_of_aKind' or combo == 'full_house':
                c1, c2 = Counter(cards), Counter(other_cards)

                if c1.most_common()[0][0] > c2.most_common()[0][0]:
                    return 'Win'
                elif c1.most_common()[0][0] < c2.most_common()[0][0]:
                    return 'Loss'
                else:
                    if c1.most_common()[-1][0] > c2.most_common()[-1][0]:
                        return 'Win'
                    else:
                        return 'Loss'

            elif combo == 'flush':
                for i in range(4, -1, -1):
                    if cards[i] < other_cards[i]:
                        return 'Loss'
                    else:
                        if cards[i] != other_cards[i]:
                            return 'Win'

            elif combo == 'three_of_aKind':
                for i in range(1, -1, -1):
                    if cards[i] < other_cards[i]:
                        return 'Loss'
                    else:
                        if cards[i] != other_cards[i]:
                            return 'Win'

            elif combo == 'two_pairs' or combo == 'pair':
                c1, c2 = Counter(cards), Counter(other_cards)
                sorted_c1 = sorted(c1.most_common(), key=lambda x: (x[1], x))
                sorted_c2 = sorted(c2.most_common(), key=lambda x: (x[1], x))

                for i in range(len(sorted_c1) - 1, -1, -1):
                    if sorted_c1[i][0] < sorted_c2[i][0]:
                        return 'Loss'
                    else:
                        if sorted_c1[i][0] != sorted_c2[i][0]:
                            return 'Win'

            else:
                for i in range(4, -1, -1):
                    if cards[i] < other_cards[i]:
                        return 'Loss'
                    else:
                        if cards[i] != other_cards[i]:
                            return 'Win'

        else:
            return 'Loss'
