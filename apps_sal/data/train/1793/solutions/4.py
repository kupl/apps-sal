class PlayingCards:

    def __init__(self):
        self.alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.factorials = [1]
        self.deck = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
                     "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
                     "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
                     "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"]

        for i in range(1, 52):
            self.factorials.append(self.factorials[-1] * i)

    def encode(self, message):
        code = self.numeral(message)
        copy = self.deck.copy()
        facts = self.factorials.copy()
        encrypted = []

        for letter in message:
            if letter not in self.alphabet:
                return None
            else:
                pass

        if code > (self.factorials[-1] * 52) - 1:
            return None

        for i in range(len(self.deck)):
            x, code = divmod(code, facts.pop())
            encrypted.append(copy[x])
            copy.remove(copy[x])

        return encrypted

    def decode(self, deck):
        copy = self.deck.copy()
        facts = self.factorials.copy()
        row = 0

        for i in range(len(self.deck)):
            try:
                if deck[i] in copy:
                    x = copy.index(deck[i])
                    row += facts.pop() * x
                    copy.remove(deck[i])
                else:
                    return None
            except:
                return None

        message = self.string(int(row), 27)
        if message == " ":
            return ''
        else:
            return message

    @staticmethod
    def numeral(string):
        return sum([((27**i) * (ord(char) - 64)) for i, char in enumerate(string.replace(" ", "@")[::-1])])

    def string(self, n, base):
        if n < base:
            return self.alphabet[n]
        else:
            return self.string(n // base, base) + self.alphabet[n % base]
