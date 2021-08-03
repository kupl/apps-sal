class Wallet(Student):
    def __init__(self, sn):
        super().__init__(sn.name, sn.fives, sn.tens, sn.twenties)

    def get_money_sum(self):
        return sum([self.fives * 5, self.tens * 10, self.twenties * 20])


class Money():
    def __init__(self, students):
        self.sns = students
        self.wallets = [Wallet(sn) for sn in students]

    def sort(self):
        return sorted(((wlt.name, wlt.get_money_sum()) for wlt in self.wallets), key=lambda tup: -tup[1])


def most_money(students):
    allmoney = Money(students).sort()
    return allmoney[0][0] if allmoney[-1][1] != allmoney[0][1] or len(allmoney) < 2 else 'all'
