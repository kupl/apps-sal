from math import factorial
stack = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']
numeral = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class PlayingCards:

    def encode(self, message):
        (tom, tim, s, deck, new) = ([], 1, 0, stack.copy(), [])
        try:
            for (i, x) in enumerate(message):
                s += numeral.index(x) * len(numeral) ** (len(message) - i - 1)
        except ValueError:
            return None
        while s >= 1:
            tom.insert(0, s % tim)
            s = s // tim
            tim += 1
        if len(tom) > 52:
            return None
        while len(tom) != 52:
            tom.insert(0, 0)
        for x in tom:
            new.append(deck[x])
            deck.remove(deck[x])
        return new

    def decode(self, new):
        (yo, haha, plus, deck) = ([], 0, [], stack.copy())
        if len(new) != 52:
            return None
        try:
            while new:
                if yo or deck.index(new[0]) != 0:
                    yo.append(deck.index(new[0]))
                deck.remove(new[0])
                new.remove(new[0])
        except ValueError:
            return None
        for (i, x) in enumerate(yo):
            haha += x * factorial(len(yo) - i - 1)
        for x in range(100000000):
            if 27 ** x > haha:
                break
        for e in reversed(range(x)):
            for b in range(27):
                if (b + 1) * 27 ** e > haha:
                    haha -= b * 27 ** e
                    plus.append(b)
                    break
        return ''.join([numeral[x] for x in plus])
