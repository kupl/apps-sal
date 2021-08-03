raw = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
layout = {char: divmod(i, 8) for i, char in enumerate(raw)}
layout['SHIFT'] = (5, 0)
layout[' '] = (5, 1)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + 1


class Keyboard:
    def __init__(self):
        self.total = 0
        self.cap = False
        self.current = (0, 0)

    def hit_shift(self):
        self.total += distance(self.current, layout['SHIFT'])
        self.cap = not self.cap
        self.current = layout['SHIFT']

    def next_letter(self, letter):
        if letter.isupper() and not self.cap:
            self.hit_shift()
        elif letter.islower() and self.cap:
            self.hit_shift()

        self.total += distance(self.current, layout[letter.lower()])
        self.current = layout[letter.lower()]

    def solve(self, word):
        for char in word:
            self.next_letter(char)


def tv_remote(words):
    k = Keyboard()
    k.solve(words)
    return k.total
