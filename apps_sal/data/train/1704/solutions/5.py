from collections import Counter


class CardValue(str):
    ORDER = "23456789TJQKA"

    def __lt__(self, other):
        return self.ORDER.index(self) < self.ORDER.index(other)

    def __gt__(self, other):
        return self.ORDER.index(self) > self.ORDER.index(other)


class Card():
    ORDER = CardValue.ORDER

    def __init__(self, card_str):
        self.value = CardValue(card_str[0])
        self.color = card_str[1]

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return "".join((self.value, self.color))


class HandValue():
    def __init__(self, poker_hand):
        self.poker_hand = poker_hand

    def compare(self, other):
        return 'Tie'

    def __str__(self):
        return self.__class__.__name__

    @property
    def pretty_string(self):
        return "{} is {}".format(self.poker_hand, self)


class RoyalFlush(HandValue):
    @staticmethod
    def is_valid(poker_hand):
        if poker_hand.is_same_color:
            if {card.value for card in poker_hand.cards} == {'A', 'K', 'Q', 'J', 'T'}:
                return True
        return False


class HighCard(HandValue):
    def compare(self, other):
        self_value_remaining = sorted(self.poker_hand.card_values, reverse=True)
        other_value_remaining = sorted(other.poker_hand.card_values, reverse=True)
        for i in range(5):
            if self_value_remaining[i] > other_value_remaining[i]:
                return 'Win'
            if self_value_remaining[i] < other_value_remaining[i]:
                return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        return True


class Pairs(HandValue):
    def compare(self, other):
        counter_self_values = Counter(self.poker_hand.card_values)
        counter_other_values = Counter(other.poker_hand.card_values)

        # Check the pair
        self_value_2 = next(value for value, nb_repet in counter_self_values.items() if nb_repet == 2)
        other_value_2 = next(value for value, nb_repet in counter_other_values.items() if nb_repet == 2)
        if self_value_2 > other_value_2:
            return 'Win'
        if self_value_2 < other_value_2:
            return 'Loss'

        # Check the remaining solo cards
        self_value_remaining = sorted((value for value, nb_repet in counter_self_values.items() if nb_repet == 1), reverse=True)
        other_value_remaining = sorted((value for value, nb_repet in counter_other_values.items() if nb_repet == 1), reverse=True)
        for i in range(3):
            if self_value_remaining[i] > other_value_remaining[i]:
                return 'Win'
            if self_value_remaining[i] < other_value_remaining[i]:
                return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        counter_values = Counter(poker_hand.card_values)
        return 2 in counter_values.values()


class TwoPairs(HandValue):
    def compare(self, other):
        counter_self_values = Counter(self.poker_hand.card_values)
        counter_other_values = Counter(other.poker_hand.card_values)

        # Check the highest pair
        max_self_value_2 = max([value for value, nb_repet in counter_self_values.items() if nb_repet == 2])
        max_other_value_2 = max([value for value, nb_repet in counter_other_values.items() if nb_repet == 2])
        if max_self_value_2 > max_other_value_2:
            return 'Win'
        if max_self_value_2 < max_other_value_2:
            return 'Loss'

        # Check the lowest pair
        min_self_value_2 = min([value for value, nb_repet in counter_self_values.items() if nb_repet == 2])
        min_other_value_2 = min([value for value, nb_repet in counter_other_values.items() if nb_repet == 2])
        if min_self_value_2 > min_other_value_2:
            return 'Win'
        if min_self_value_2 < min_other_value_2:
            return 'Loss'

        # Otherwise check the lowest remaining value
        self_value_1 = next(value for value, nb_repet in counter_self_values.items() if nb_repet == 1)
        other_value_1 = next(value for value, nb_repet in counter_other_values.items() if nb_repet == 1)
        if self_value_1 > other_value_1:
            return 'Win'
        if self_value_1 < other_value_1:
            return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        counter_values = Counter(poker_hand.card_values)
        return list(counter_values.values()).count(2) == 2


class ThreeOfAKind(HandValue):
    def compare(self, other):
        counter_self_values = Counter(self.poker_hand.card_values)
        counter_other_values = Counter(other.poker_hand.card_values)

        # Check the value of the 3 of a kind
        max_self_value_3 = [value for value, nb_repet in counter_self_values.items() if nb_repet == 3][0]
        max_other_value_3 = [value for value, nb_repet in counter_other_values.items() if nb_repet == 3][0]
        if max_self_value_3 > max_other_value_3:
            return 'Win'
        if max_self_value_3 < max_other_value_3:
            return 'Loss'

        # Check the highest remaining value
        max_self_value_2 = max(value for value, nb_repet in counter_self_values.items() if nb_repet == 1)
        max_other_value_2 = max(value for value, nb_repet in counter_other_values.items() if nb_repet == 1)
        if max_self_value_2 > max_other_value_2:
            return 'Win'
        if max_self_value_2 < max_other_value_2:
            return 'Loss'

        # Otherwise check the lowest remaining value
        min_self_value_2 = min(value for value, nb_repet in counter_self_values.items() if nb_repet == 1)
        min_other_value_2 = min(value for value, nb_repet in counter_other_values.items() if nb_repet == 1)
        if min_self_value_2 > min_other_value_2:
            return 'Win'
        if min_self_value_2 < min_other_value_2:
            return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        counter_self_values = Counter(poker_hand.card_values)
        return 3 in counter_self_values.values()


class FullHouse(HandValue):
    def compare(self, other):
        counter_self_values = Counter(self.poker_hand.card_values)
        counter_other_values = Counter(other.poker_hand.card_values)

        # Check the value of the 3 of a kind
        max_self_value_3 = [value for value, nb_repet in counter_self_values.items() if nb_repet == 3][0]
        max_other_value_3 = [value for value, nb_repet in counter_other_values.items() if nb_repet == 3][0]
        if max_self_value_3 > max_other_value_3:
            return 'Win'
        if max_self_value_3 < max_other_value_3:
            return 'Loss'

        # Case 3 of a kind value is the same, check pair value
        max_self_value_2 = [value for value, nb_repet in counter_self_values.items() if nb_repet == 2][0]
        max_other_value_2 = [value for value, nb_repet in counter_other_values.items() if nb_repet == 2][0]
        if max_self_value_2 > max_other_value_2:
            return 'Win'
        if max_self_value_2 < max_other_value_2:
            return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        counter_self_values = Counter(poker_hand.card_values)
        return set(counter_self_values.values()) == {2, 3}


class FourOfAKind(HandValue):
    def compare(self, other):
        counter_self_values = Counter(self.poker_hand.card_values)
        counter_other_values = Counter(other.poker_hand.card_values)
        max_self_value = [value for value, nb_repet in counter_self_values.items() if nb_repet == 4][0]
        max_other_value = [value for value, nb_repet in counter_other_values.items() if nb_repet == 4][0]
        if max_self_value > max_other_value:
            return 'Win'
        if max_self_value < max_other_value:
            return 'Loss'

        max_self_value = [value for value, nb_repet in counter_self_values.items() if nb_repet == 1][0]
        max_other_value = [value for value, nb_repet in counter_other_values.items() if nb_repet == 1][0]
        if max_self_value > max_other_value:
            return 'Win'
        if max_self_value < max_other_value:
            return 'Loss'
        return 'Tie'


    @staticmethod
    def is_valid(poker_hand):
        counter_self_values = Counter(poker_hand.card_values)
        return 4 in counter_self_values.values()


class Straight(HandValue):
    def compare(self, other):
        max_self_value = max(self.poker_hand.card_values)
        max_other_value = max(other.poker_hand.card_values)
        if max_self_value > max_other_value:
            return 'Win'
        if max_self_value < max_other_value:
            return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        sorted_values = list(sorted(Card.ORDER.index(card.value) for card in poker_hand.cards))
        return sorted_values == list(range(sorted_values[0], sorted_values[0] + 5))


class Flush(HandValue):
    def compare(self, other):
        return HighCard.compare(self, other)


    @staticmethod
    def is_valid(poker_hand):
        return poker_hand.is_same_color


class StraightFlush(HandValue):
    def compare(self, other):
        max_self_value = max(self.poker_hand.card_values)
        max_other_value = max(other.poker_hand.card_values)
        if max_self_value > max_other_value:
            return 'Win'
        if max_self_value < max_other_value:
            return 'Loss'
        return 'Tie'

    @staticmethod
    def is_valid(poker_hand):
        if poker_hand.is_same_color:
            sorted_values = list(sorted(Card.ORDER.index(card.value) for card in poker_hand.cards))
            return sorted_values == list(range(sorted_values[0], sorted_values[0] + 5))
        return False


class PokerHand(object):
    RESULT = ['Loss', 'Tie', 'Win']
    HV_ORDER = [HighCard,
                Pairs,
                TwoPairs,
                ThreeOfAKind,
                Straight,
                Flush,
                FullHouse,
                FourOfAKind,
                StraightFlush,
                RoyalFlush]

    def __init__(self, hand):
        self.cards = tuple(Card(card_str) for card_str in hand.split())
        self.is_same_color = (len(set(self.card_colors)) == 1)
        self.hand_value = None
        for hand_value_cls in reversed(self.HV_ORDER):
            if hand_value_cls.is_valid(self):
                # print("{} is {}".format(hand, hand_value_cls.__name__))
                self.hand_value = hand_value_cls(self)
                break

    def __str__(self):
        return " ".join(map(str, self.cards))

    def compare_with(self, other):
        print(self.hand_value.pretty_string)
        print(other.hand_value.pretty_string)
        if self.HV_ORDER.index(type(self.hand_value)) < self.HV_ORDER.index(type(other.hand_value)):
            return 'Loss'
        if self.HV_ORDER.index(type(self.hand_value)) > self.HV_ORDER.index(type(other.hand_value)):
            return 'Win'
        return self.hand_value.compare(other.hand_value)

    @property
    def card_values(self):
        return tuple(card.value for card in self.cards)

    @property
    def card_colors(self):
        return tuple(card.color for card in self.cards)
