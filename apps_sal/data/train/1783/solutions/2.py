class PokerHand(object):
    ''' The class represent a poker hand at Texas Holdem Poker.
        A hand consists of 5 best cards from 7 cards(2-pocket, 5-table).
        And this 5 cards is a combination, each combination have a value.
        The hand with a larger value - wins.

        The class contains following functions:
            * hand_to_vector - converts a hand in vector of count cards
            * combination - returns the name of the combination of a hand
            * value - returns the value of the combination (can be compared with another hand)
            * compare_with - compares the instance hand with other hand
    '''

    def __init__(self, hand):
        self.hand = hand
        self.hand_value = self.value(hand)

    def __repr__(self): return self.hand

    def __lt__(self, other): return self.hand_value > other.hand_value
    def __eq__(self, other): return self.hand_value == other.hand_value

    def compare_with(self, other):
        ''' Compares 2 hands: first - instance hand, second - param
            Args:
                other (PokerHand): Another instance of PokerHand
            Returns:
                str: the result of the game if our and another hand were played
        '''
        if self.hand_value > other.hand_value:
            return 'Win'
        elif self.hand_value < other.hand_value:
            return 'Loss'
        elif self.hand_value == other.hand_value:
            return 'Tie'

    @staticmethod
    def hand_to_vector(hand):
        ''' Parse a hand in a vector, where a value of the vector is count of cards
            card:     2  3  4      K  A
            vector:  [0, 0, 0, ... 0, 0]    
        Args:
            hand (str): A combination of five cards, example '2S AH 4H 5S 6C'
        Returns:
            list: A vector of count of cards
        '''
        vec_hand = [0] * 13
        for card in hand.split():
            try:
                vec_hand[int(card[0]) - 2] += 1
            except:
                switcher = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8}
                vec_hand[switcher[card[0]]] += 1
        return vec_hand

    @staticmethod
    def combination(hand):
        ''' Firuers out the combination of the hand
        Args:
            hand (str): A combination of five cards, example '2S AH 4H 5S 6C'
        Returns:
            str: the name of the combination
        '''
        vec_hand = PokerHand.hand_to_vector(hand)
        # suited --> True, when all cards of the same suit
        suited = False
        if 1 == len(set([x[1] for x in hand.split()])):
            suited = True

        if 4 in vec_hand:
            return 'Four of a kind'
        else:
            if 3 in vec_hand:
                if 2 in vec_hand:
                    return 'Full house'
                else:
                    return 'Three of a kind'
            else:
                if 2 in vec_hand:
                    if 2 == vec_hand.count(2):
                        return 'Two pair'
                    else:
                        return 'One pair'
                if '11111' not in ''.join([str(x) for x in (vec_hand[-1:] + vec_hand)]):
                    if suited:
                        return 'Flush'
                    else:
                        return 'High card'
                else:
                    if not suited:
                        return 'Straight'
                    else:
                        if vec_hand[8] == 1 and vec_hand[12] == 1:
                            return 'Royal flush'
                        else:
                            return 'Straight flush'

    @staticmethod
    def value(hand):
        ''' Calculates the value of the hand
        Args:
            hand (str): A combination of five cards, example '2S AH 4H 5S 6C'
        Returns:
            int: the value of the hand
        '''
        hand_vec = PokerHand.hand_to_vector(hand)
        ''' value_vec - a splited binary number, where each section represents
            a specific combination
            [ Straight flush, Care, Full house(set), Full house(pair), Flush, Straight,
              Two pair(Hihg pair), Two pair(Low pair), One pair ]
        '''
        value_vec = ['0', '0000', '0000', '0000', '0', '0', '0000', '0000', '0000', '0000']
        combination = PokerHand.combination(hand)
        if combination == 'One pair':
            value_vec[9] = '{:04b}'.format(hand_vec.index(2))
        elif combination == 'Two pair':
            value_vec[8] = '{:04b}'.format(hand_vec.index(2))
            value_vec[7] = '{:04b}'.format(hand_vec.index(2, hand_vec.index(2) + 1))
        elif combination == 'Three of a kind':
            value_vec[6] = '{:04b}'.format(hand_vec.index(3))
        elif combination == 'Straight':
            value_vec[5] = '1'
            if hand_vec[12] == 1 and hand_vec[3] == 1:
                hand_vec[12] = 0
        elif combination == 'Flush':
            value_vec[4] = '1'
        elif combination == 'Full house':
            value_vec[3] = '{:04b}'.format(hand_vec.index(2))
            value_vec[2] = '{:04b}'.format(hand_vec.index(3))
        elif combination == 'Four of a kind':
            value_vec[1] = '{:04b}'.format(hand_vec.index(4))
        elif combination == 'Straight flush':
            value_vec[0] = '1'
            if hand_vec[12] == 1 and hand_vec[3] == 1:
                hand_vec[12] = 0
        elif combination == 'Royal flush':
            value_vec[0] = '1'
            value_vec[1] = '1111'

        ''' The result is binary number: value_vec extended 
            with hand_vec(contains only 0/1, to represent remaining single cards),
            and this resulting extended binary number convert to decimal.
        '''
        return int(''.join(value_vec) + ''.join(reversed(list([str(x) if x == 1 else str(0) for x in hand_vec]))), 2)
