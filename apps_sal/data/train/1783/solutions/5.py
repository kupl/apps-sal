from collections import defaultdict
from typing import List


class PokerHand(object):
    '''Representation of a poker hand and its basic characteristics.

    The PokerHands Weight are:
        Straight Flush  : 1
        Four of a Kind  : 2
        Full House      : 3
        Flush           : 4
        Straight        : 5
        Three of a Kind : 6
        Two Pairs       : 7
        Pair            : 8
        High Card       : 9

    In the sample test, the sorted poker hands are displayed with the highest ranking hand in the top.
    The sort method, sorts in ascending order, this means the highest weight would have to be considered the lowest number.

    If there are ties between the hands weight, the tiebreaker shall be resolved as follow:
        Straight Flush or Straight:
            The hand with the highest card in the Straight.
            There's no need to account for the Royal Straight Flush because of this.
        Four of a Kind:
            The highest Four of a Kind, then the Kicker.
        Full House:
            The highest Three of a Kind, then the highest Pair.
        Flush:
            The hand with the highest card in the Flush wins.
        Three of a Kind:
            The highest Three of a Kind, then the highest Kicker.
        Two Pairs or Pair:
            The highest Pair, then the highest Kicker.
        High Card:
            The highest card in the hand.

    If still there is a tie, then it is a tie because all the Suits have the same weight.

    Attributes:
        hand (str): String representation of the poker hand.
        cards (List[PokerCard]): The list of poker cards in this hand.
    '''

    def __repr__(self):
        return self.hand

    def __init__(self, hand: str):
        self.hand = hand
        self.cards = [PokerCard(card) for card in hand.split(' ')]
        self.cards.sort()
        self.hand_weight = self._calculate_hand_weight()

    def __eq__(self, other):
        if self.hand_weight[0] != other.hand_weight[0]:
            return False

        for i in range(1, len(self.hand_weight)):
            if self.hand_weight[i] != other.hand_weight[i]:
                return False
        return True

    def __lt__(self, other):
        if self.hand_weight[0] < other.hand_weight[0]:
            return True

        if self.hand_weight[0] == other.hand_weight[0]:
            for i in range(1, len(self.hand_weight)):
                if self.hand_weight[i] == other.hand_weight[i]:
                    continue
                if self.hand_weight[i] < other.hand_weight[i]:
                    return True
                return False
        return False

    def _calculate_hand_weight(self):
        '''Analize hand strenght.

        Returns:
            A Tuple containing the hand weight as its firs argument,
            then the cards ranks to break a tie in case the hand weight is the same.
        '''
        hand = defaultdict(int)
        for card in self.cards:
            hand[card.rank] += 1

        length = len(hand)
        values = list(hand.values())

        if length == 5:
            suited = self.is_suited()
            straight_high_card = self.is_a_straight()

            if suited and straight_high_card:
                return (1, straight_high_card)
            if suited:
                return (4, *self.cards)
            if straight_high_card:
                return (5, straight_high_card)
            return (9, *self.cards)

        if length == 2:
            if 4 in values:
                i_four = values.index(4)
                i_kicker = values.index(1)
                return (2, self.cards[i_four], self.cards[i_kicker])

            i_triple = values.index(3)
            i_pair = values.index(2)
            return (3, self.cards[i_triple], self.cards[i_pair])

        if length == 3:
            if 3 in values:
                i_triple = values.index(3)
                return (6, self.cards[i_triple], *self.cards[:i_triple], *self.cards[i_triple + 1:])

            i_pair = values.index(2)
            j_pair = values.index(2, i_pair + 1)
            i_kicker = values.index(1)
            return (7, self.cards[i_pair], self.cards[j_pair], self.cards[i_kicker])

        if length == 4:
            i_pair = values.index(2)
            return (8, self.cards[i_pair], *self.cards[:i_pair], *self.cards[i_pair + 1:])

    def is_suited(self):
        '''Check if hand is Suited.'''
        for i in range(len(self.cards) - 1):
            if self.cards[i].suit != self.cards[i + 1].suit:
                return False

        return True

    def is_a_straight(self):
        '''Check if hand is a Straight

        Returns:
            The highest card in the Straight.
        '''
        starter = 0
        if self.cards[0].rank == 'A' and self.cards[1].rank == '5':
            starter = 1

        for i in range(starter, len(self.cards) - 1):
            if self.cards[i + 1] - self.cards[i] != 1:
                return False

        if starter == 1:
            return self.cards[1]

        return self.cards[0]


class PokerCard(object):
    '''Representation of a poker card and its basic characteristics.

    The PokerCards Weight are:
        Ace:    1       |   7:      8
        King:   2       |   6:      9
        Queen:  3       |   5:      10
        Jack:   4       |   4:      11
        Ten:    5       |   3:      12
        9:      6       |   2:      13
        8:      7       |   Ace*:   When comparing it in a low Straight

    Attributes:
        card (str): String representation of the poker card.
        rank (str): The rank of the card.
        suit (str): The suit of the card.
    '''

    def __repr__(self):
        return self.card_weight

    def __init__(self, card: str):
        self.card = card
        self.rank = card[0]
        self.suit = card[1]
        self.card_weight = self.get_card_weight()

    def __eq__(self, other):
        return True if self.card_weight == other.card_weight else False

    def __lt__(self, other):
        return True if self.card_weight < other.card_weight else False

    def __sub__(self, other):
        return self.card_weight - other.card_weight

    def get_card_weight(self):
        '''Return the card weight based on its rank.'''
        if self.rank == 'T':
            return 5
        if self.rank == 'J':
            return 4
        if self.rank == 'Q':
            return 3
        if self.rank == 'K':
            return 2
        if self.rank == 'A':
            return 1
        return (63 - ord(self.rank))
