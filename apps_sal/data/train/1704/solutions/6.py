class PokerHand(object):

    def __init__(self, hand):
        self.hand = hand
        self.lst = ['10' if 'T' in x else x[0].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in self.hand.split()]

    def straight(self):
        return 0 if not ''.join(sorted(self.lst, key=int)) in '234567891011121314' else max(list(map(int, self.lst)))

    def four(self):
        return 0 if not max([self.lst.count(x) for x in self.lst]) == 4 else [x for x in self.lst if self.lst.count(x) == 4][0]

    def full_house(self):
        return 0 if not len(set(self.lst)) == 2 or self.four() != 0 else [x for x in self.lst if self.lst.count(x) == 3][0]

    def flush(self):
        return 0 if not len({x[-1] for x in self.hand.split()}) == 1 or self.full_house() or self.four() else 6

    def three(self):
        return 0 if not max([self.lst.count(x) for x in self.lst]) == 3 or self.full_house() else [x for x in self.lst if self.lst.count(x) == 3][0]

    def two_pair(self):
        return 0 if not len(set(self.lst)) == 3 or self.three() else max({x for x in self.lst if self.lst.count(x) == 2}, key=int)

    def pair(self):
        return 0 if not len(set(self.lst)) == 4 else max({x for x in self.lst if self.lst.count(x) == 2}, key=int)

    def high(self):
        return sum(map(int, self.lst))

    def score(self):
        out = list(map(int, [min(self.straight(), self.flush()), self.four(), self.full_house(), self.flush(), self.straight(), self.three(), self.two_pair(), self.pair(), self.high()]))
        b = 14
        return out[0] * b ** 8 + out[1] * b ** 7 + out[2] * b ** 6 + out[3] * b ** 5 + out[4] * b ** 4 + out[5] * b ** 3 + out[6] * b ** 2 + out[7] * b ** 1 + out[8]

    def final_check(self, other):
        (one, two) = [sorted(x, key=int, reverse=True) for x in (self.lst, other.lst)]
        for i in range(5):
            if int(one[i]) > int(two[i]):
                return 1
            if int(two[i]) > int(one[i]):
                return -1
        return 0

    def compare_with(self, other):
        RESULT = ['Loss', 'Win']
        if self.score() == other.score() and (not self.final_check(other)):
            return 'Tie'
        if not self.straight() and (not self.flush()) and (not self.four()) and (not self.full_house()) and (not self.flush()) and (not self.straight()) and (not self.three()) and (not self.two_pair()) and (not self.pair()) and (not other.straight()) and (not other.flush()) and (not other.four()) and (not other.full_house()) and (not other.flush()) and (not other.straight()) and (not other.three()) and (not other.two_pair()) and (not other.pair()):
            return RESULT[self.final_check(other) > 0]
        return RESULT[self.score() > other.score()]
