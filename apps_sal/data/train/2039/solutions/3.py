# AC
import sys


class Main:
    def __init__(self):
        self.buff = None
        self.index = 0

    def __next__(self):
        if self.buff is None or self.index == len(self.buff):
            self.buff = self.next_line()
            self.index = 0
        val = self.buff[self.index]
        self.index += 1
        return val

    def next_line(self):
        return sys.stdin.readline().split()

    def next_ints(self):
        return [int(x) for x in sys.stdin.readline().split()]

    def next_int(self):
        return int(next(self))

    def solve(self):
        n, m = self.next_ints()
        x = self.next_ints()
        low = 0
        high = m
        while high - low > 1:
            mid = (high + low) // 2
            if self.test(mid, x, m):
                high = mid
            else:
                low = mid
        print(low if self.test(low, x, m) else high)

    def test(self, st, xs, m):
        xx = 0
        for x in xs:
            fr = x
            to = x + st
            if to >= m:
                to -= m
            if to >= fr:
                if xx > to:
                    return False
                xx = max(xx, fr)
            elif to < xx < fr:
                xx = fr
        return True


def __starting_point():
    Main().solve()


__starting_point()
