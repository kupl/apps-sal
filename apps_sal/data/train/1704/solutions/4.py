class PokerHand(object):
    FACE_VALUE = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, hand):
        self.suits = {"S": 0, "H": 0, "D": 0, "C": 0}
        self.values = {}
        self.flush = False
        for card in hand.split():
            card_val = self.FACE_VALUE.get(card[0])
            self.values[card_val] = self.values.get(card_val, 0) + 1
            self.suits[card[1]] += 1
            if self.suits[card[1]] == 5:
                self.flush = True
        self.high_low = self.high_low()
        self.straight = self.look_for_straight()
        self.rank_high_low = [self.rank()] + self.high_low[:]

    def high_low(self):
        high_low = []
        for i in range(1, 5):
            high_low += sorted([k for k, v in self.values.items() if v == i])
        return high_low[::-1]

    def look_for_straight(self):
        val_array = self.high_low[:]
        if 14 in val_array:
            val_array[val_array.index(14)] = 1 if 2 in val_array else 14
        return val_array == list(range(val_array[0], val_array[0] - 5, -1))

    def rank(self):
        num_vals = list(self.values.values())
        if self.flush:
            return 9 if self.straight else 6
        if num_vals.count(4) == 1:
            return 8
        if num_vals.count(3) == 1:
            return 7 if num_vals.count(2) == 1 else 4
        if self.straight:
            return 5
        if num_vals.count(2) > 0:
            return 3 if num_vals.count(2) == 2 else 2
        return 1

    def compare_with(self, other):
        for i in range(len(self.rank_high_low)):
            if self.rank_high_low[i] > other.rank_high_low[i]:
                return "Win"
            if self.rank_high_low[i] < other.rank_high_low[i]:
                return "Loss"
        return "Tie"
