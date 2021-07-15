import string


class PlayingCards:
    CHARSET = " " + string.ascii_uppercase
    DECK = [card + suit for suit in "CDHS" for card in "A23456789TJQK"]
    DECKSIZE = len(DECK)
    MAX_FACT = 80658175170943878571660636856403766975289505440883277824000000000000 # 52!

    def encode(self, msg: string):
        # validate input
        if any(c not in self.CHARSET for c in msg):
            return None

        # calculate desired permutation index from input message
        perm_index = sum(self.CHARSET.index(c) * pow(27, i) for i, c in enumerate(reversed(msg)))
        if perm_index >= self.MAX_FACT:
            # index too large, invalid input
            return None

        # calculate factoradic (factorial representation)
        frep = []
        i = 0
        while perm_index:
            i += 1
            frep.append(perm_index % i)
            perm_index = perm_index // i
        frep.reverse()

        # return deck permutation 
        left_part = self.DECK[: self.DECKSIZE - len(frep)]
        right_part = self.DECK[self.DECKSIZE - len(frep) :]
        return left_part + [right_part.pop(pos) for pos in frep]


    def decode(self, input_deck: list):
        # validate input
        if any(card not in self.DECK for card in input_deck) or len(set(input_deck)) != self.DECKSIZE:
            return None
        
        # find permutation index of input deck
        j = 0
        perm_index = 0
        while j < self.DECKSIZE:
            i = 1
            factor = 1
            while i < self.DECKSIZE - j:
                factor *= i
                i += 1
            i = 0
            index = self.DECK.index(input_deck[j])
            while i < j:
                if self.DECK.index(input_deck[i]) < self.DECK.index(input_deck[j]):
                    index -= 1
                i += 1
            perm_index += index * factor
            j += 1

        # convert deck permutation index to message
        message = ''
        i = 0
        while perm_index:
            i += 1
            message = self.CHARSET[perm_index % 27] + message
            perm_index = perm_index // 27
        return message

