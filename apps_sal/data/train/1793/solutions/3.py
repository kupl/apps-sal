import math
import numpy as np
d = {
    " ": 0,
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": "A",
    "K": "B",
    "L": "C",
    "M": "D",
    "N": "E",
    "O": "F",
    "P": "G",
    "Q": "H",
    "R": "I",
    "S": "J",
    "T": "K",
    "U": "L",
    "V": "M",
    "W": "N",
    "X": "O",
    "Y": "P",
    "Z": "Q"

}

s_deck = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD", "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"]


class PlayingCards:

    def encode(self, message):

        if message == "":
            message = " "

        if len(message) > 52:
            return None

        meslis = [str(x) for x in message]
        for i in range(len(meslis)):
            if meslis[i] in d:
                None
            else:
                return None

        bnum = "".join([str(d[x]) for x in message])
        num = int(bnum, 27)
        if num >= math.factorial(52):
            return None

        fact = []
        for j in range(1, 53):
            fact.insert(0, num % j)
            num = int(num // j)

        final = ["

        s_deckc = s_deck.copy()

        for v in range(0, 52):
            final[v] = s_deckc[fact[v]]
            del s_deckc[fact[v]]

        return final

    def decode(self, deck):

        s_deckc = s_deck.copy()

        if len(deck) != 52:
            return None

        dfact = []
        numb = 0
        for i in range(52):
            if deck[i] in s_deckc:
                None
            else:
                return None
            fact = int(s_deckc.index(deck[i]))
            del s_deckc[fact]
            numb += fact * math.factorial(51 - i)

        if numb == 0:
            return ""

        basetws = np.base_repr(numb, base=27)
        btws_list = [str(x) for x in basetws]
        r_d = {str(value): str(key) for (key, value) in d.items()}

        word = []

        for i in range(len(btws_list)):
            word.append(r_d[btws_list[i]])
        return "".join(word)
