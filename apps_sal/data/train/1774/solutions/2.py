class Funnel:

    def __init__(self):
        self.funnel = [[' ' for j in range(i + 1)] for i in range(5)]
        self.data = 0

    def fill(self, *args):
        for arg in args:
            if self.data < 15:
                for (indexi, i) in enumerate(self.funnel):
                    if ' ' in i:
                        self.funnel[indexi][i.index(' ')] = str(arg)
                        self.data += 1
                        break

    def count_weight_left(self, row, index):
        if self.funnel[row][index] != ' ':
            if row < 4:
                return 1 + self.count_weight_left(row + 1, index)
            else:
                return 1
        return 0

    def count_weight_both(self, row, index):
        if self.funnel[row][index] != ' ':
            if row < 4:
                return 1 + self.count_weight_left(row + 1, index) + self.count_weight_both(row + 1, index + 1)
            else:
                return 1
        return 0

    def drip(self):
        if not self.data:
            return None
        self.data -= 1
        value = int(self.funnel[0][0])
        index = 0
        for row in range(1, 5):
            if self.count_weight_both(row, index) >= self.count_weight_both(row, index + 1):
                self.funnel[row - 1][index] = self.funnel[row][index]
                self.funnel[row][index] = ' '
            else:
                self.funnel[row - 1][index] = self.funnel[row][index + 1]
                index += 1
                self.funnel[row][index] = ' '
        return value

    def __str__(self):
        string = ''
        for (index, i) in enumerate(reversed(self.funnel)):
            string += ' ' * index + '\\' + ' '.join(i) + '/\n'
        return string[:-1]
