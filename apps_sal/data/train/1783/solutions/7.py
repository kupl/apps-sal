from typing import Tuple, List
from functools import total_ordering


@total_ordering
class PokerHand(object):
    """Create an object representing a Poker Hand based on an input of a
    string which represents the best 5 card combination from the player's hand
    and board cards.

    Attributes:
        hand: string representating the hand consisting of five cards
        cards: list of two tuple containing the value of the card and suit
            in sorted order
        hand value: total hand value of all the cards
        hand type: hand type as a number from the list given in docstring of
            hand_type function
        high card: value of the high card in a given hand

    Methods:
        compare_with(self, opponent): takes in player's hand (self) and
            opponent's hand (opponent) and compares both hands according to
            rules of Texas Hold'em.
            Returns one of 3 strings (Win, Loss, Tie) based on whether
            player's hand is better than opponent's hand.

    Helper Methods:
        _hand_with_values: Internal representation of hand as a list of two
            tuple containing the value of the card and suit in sorted order
        _is_flush: Determine whether a hand is flush or not
        _is_straight: Determine whether a hand is straight or not
        _is_same_kind: Determine whether a hand is of any kind (Look at doc
            for complete list)
        _hand_type: represent hand type as a number in order of precedence
        _high_card: Value of the highest card to break the tie in straight or
            straight flush
        _total_hand_value: Total value of the hand
        _compare_cards: Compare each cards from self and other
        _tie_breaker: To determine the outcome if self and other are of same
            type
    """

    def __init__(self, hand: str):
        self._hand = hand
        self._cards = self._hand_with_values()
        self._hand_value = self._total_hand_value()
        self._hand_type = self._hand_type()
        self._high_card = self._high_card()
        self._first_pair = 0
        self._second_pair = 0

    def compare_with(self, other: 'PokerHand') -> str:
        """
        Determines the outcome of the comparing self hand with other hand.
        Returns the output either 'Win', 'Loss', 'Tie' accordingly.
        :type other: PokerHand
        """
        if self._hand_type > other._hand_type:
            return 'Win'
        elif self._hand_type < other._hand_type:
            return 'Loss'
        else:
            return self._tie_breaker(other, self._hand_type)

    def _tie_breaker(self, other: 'PokerHand', hand_type: int) -> str:
        """
        This method is used to break the tie if self hand and other hand
        has same type.
        For royal flush, it can only be a Tie.
        For straigh flush or straight compare the high card.
        For four of a kind or full house compare the first pair and if they
            are same then compare the hand value.
        For three of a kind or one pair, compare the first pair and if they
            are same then compare all the cards in reverse order as the cards
            are sorted.
        For two pairs, compare the first pair and then the second pair and if
            both are the same then compare the hand value.
        For flush and high card, compare all the cards in reverse order.
        :type other: PokerHand
        """
        if hand_type == 23:
            return 'Tie'
        elif hand_type in [22, 18]:
            return 'Win' if self._high_card > other._high_card else 'Loss' if self._high_card < other._high_card else 'Tie'
        elif hand_type in [21, 20]:
            if self._first_pair == other._first_pair:
                return 'Win' if self._hand_value > other._hand_value else 'Loss' if self._hand_value < other._hand_value else 'Tie'
            return 'Win' if self._first_pair > other._first_pair else 'Loss'
        elif hand_type in [17, 15]:
            if self._first_pair == other._first_pair:
                return self._compare_cards(other)
            return 'Win' if self._first_pair > other._first_pair else 'Loss'
        elif hand_type == 16:
            if self._first_pair == other._first_pair:
                if self._second_pair == other._second_pair:
                    return 'Win' if self._hand_value > other._hand_value else 'Loss' if self._hand_value < other._hand_value else 'Tie'
                else:
                    return 'Win' if self._second_pair > other._second_pair else 'Loss'
            return 'Win' if self._first_pair > other._first_pair else 'Loss'
        else:
            return self._compare_cards(other)

    def _compare_cards(self, other: 'PokerHand') -> str:
        """Comparing all the cards from its highest value to the lowest
        and accordingly returns either 'Win', 'Loss', 'Tie'.
        :type other: PokerHand
        """
        for i in range(4, -1, -1):
            if self._cards[i][0] != other._cards[i][0]:
                return 'Win' if self._cards[i][0] > other._cards[i][0] else 'Loss'
        return 'Tie'

    def _hand_type(self) -> int:
        """
        Determine the type of hand.
        Returns the value from the following table:
        23: Royal flush
        22: Straight flush
        21: Four of a kind
        20: Full house
        19: Flush
        18: Straight
        17: Three of a kind
        16: Two pairs
        15: One pair
        14: Decide with highest card
        """
        if self._is_flush() and (self._is_five_high_straight() or self._is_straight()):
            if self._hand_value == 60:
                return 23
            else:
                return 22
        elif self._is_flush():
            return 19
        elif self._is_five_high_straight() or self._is_straight():
            return 18
        elif self._is_same_kind():
            kind_type = self._is_same_kind()
            return 14 + kind_type
        else:
            return 14

    def _high_card(self) -> int:
        """Return the value of highest card in a hand"""
        return self._cards[-1][0]

    def _total_hand_value(self) -> int:
        """Return the total hand value"""
        return sum((card[0] for card in self._cards))

    def _is_flush(self) -> bool:
        """
        Determine whether hand is a flush or not.
        Returns True or False
        """
        suit = self._cards[0][-1]
        return all(map(lambda card: suit in card, self._cards))

    def _is_five_high_straight(self) -> bool:
        """
        Determine whether a hand is a five high straight (low ace)
        If it is change the location of ace from the end of the list to the
        start otherwise don't do anything. If asked again then don't pop the
        last element again. Check whether the last element is ace or not.
        Returns True or False
        """
        if self._hand_value == 28:
            if self._cards[-1][0] == 14:
                ace_card = self._cards.pop()
                self._cards.insert(0, ace_card)
            return True
        return False

    def _is_straight(self) -> bool:
        """
        Determine whether hand is straight or not.
        Returns True or False.
        """
        for i in range(4):
            if self._cards[i + 1][0] - self._cards[i][0] != 1:
                return False
        return True

    def _is_same_kind(self) -> int:
        """
        Determine the kind of hand if it is any and assign the value of the
        first and second pair to the respective attributes.
        Returns kind value else False.
        Kind Values:
        7: Four of a kind
        6: Full house
        3: Three of a kind
        2: Two pairs
        1: One pair
        0: False
        """
        kind = val1 = val2 = 0
        for i in range(4):
            if self._cards[i][0] == self._cards[i + 1][0]:
                if not val1:
                    val1 = self._cards[i][0]
                    kind += 1
                elif val1 == self._cards[i][0]:
                    kind += 2
                elif not val2:
                    val2 = self._cards[i][0]
                    kind += 1
                elif val2 == self._cards[i][0]:
                    kind += 2
        kind = kind + 2 if kind in [4, 5] else kind
        self._first_pair = max(val1, val2)
        self._second_pair = min(val1, val2)
        return kind

    def _hand_with_values(self) -> List[Tuple[int, str]]:
        """
        Subsitute word values with int values and convert the hand into
        2-tuple lists having the values (value, suit).
        Returns the sorted hand with the above changes.
        """
        trans = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
        new_hand = self._hand.translate(str.maketrans(trans)).split()
        final_hand = [(int(card[:-1]), card[-1]) for card in new_hand]
        return sorted(final_hand)

    def __repr__(self):
        return self._hand

    def __str__(self):
        return self._hand

    def __lt__(self, other: 'PokerHand'):
        outcome = self.compare_with(other)
        return True if outcome == 'Win' else False

    def __eq__(self, other: 'PokerHand'):
        outcome = self.compare_with(other)
        return True if outcome == 'Tie' else False
