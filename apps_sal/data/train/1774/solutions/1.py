class Funnel(object):
    above = ((1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (10, 11), (11, 12), (12, 13), (13, 14))
    weight = (None, (3, 4, 6, 7, 8, 10, 11, 12, 13), (4, 5, 7, 8, 9, 11, 12, 13, 14), (6, 7, 10, 11, 12), (7, 8, 11, 12, 13), (8, 9, 12, 13, 14), (10, 11), (11, 12), (12, 13), (13, 14))

    def __init__(self):
        self.f = [' '] * 15

    def fill(self, *args):
        i = 0
        for x in args:
            while i < 15 and self.f[i] != ' ':
                i += 1
            if i == 15:
                break
            self.f[i] = x

    def drip(self):
        if self.f[0] == ' ':
            return

        def helper(i):
            return (self.f[i] != ' ', i < 10 and sum((self.f[j] != ' ' for j in Funnel.weight[i])) + 1)
        (res, self.f[0]) = (self.f[0], ' ')

        def rec(i=0):
            if i < 10 and self.f[i] == ' ':
                j = max(Funnel.above[i], key=helper)
                (self.f[i], self.f[j]) = (self.f[j], ' ')
                rec(j)
        return rec() or res

    def __str__(self):
        return '\\{10} {11} {12} {13} {14}/\n \\{6} {7} {8} {9}/\n  \\{3} {4} {5}/\n   \\{1} {2}/\n    \\{0}/'.format(*self.f)
