class PlayingCards:
    CARDS = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']
    S = len(CARDS)

    def __init__(self):
        self.f = [0] * self.S
        self.f[0] = 1
        for k in range(1, self.S):
            self.f[k] = self.f[k - 1] * k
        self.CARD_index = {c: self.CARDS.index(c) for c in self.CARDS}

    def baseEncode(self, s):
        r = 0
        for c in s:
            r *= 27
            r += ord(c) % 32
        return r

    def baseDecode(self, n):
        s = ''
        while n:
            (n, c) = divmod(n, 27)
            s = (chr(64 + c) if c else ' ') + s
        return s

    def permute(self, n):
        S = 52
        p = [0] * S
        for k in range(S):
            (p[k], n) = divmod(n, self.f[S - 1 - k])
        for k in range(S - 1, 0, -1):
            for j in range(k - 1, -1, -1):
                if p[j] <= p[k]:
                    p[k] += 1
        return [self.CARDS[i] for i in p]

    def encode(self, message):
        if not all((c == ' ' or 'A' <= c <= 'Z' for c in message)):
            return
        n = self.baseEncode(message)
        if n >= 80658175170943878571660636856403766975289505440883277824000000000000:
            return
        p = self.permute(n)
        return p

    def decode(self, deck):
        if set(deck) != set(self.CARDS):
            return
        (i, j) = (0, 1)
        perm = [self.CARD_index[c] for c in deck]
        for p in range(50, -1, -1):
            s = 0
            for q in range(p + 1, 52):
                if perm[p] > perm[q]:
                    s += 1
            i += s * self.f[j]
            j += 1
        return self.baseDecode(i)
