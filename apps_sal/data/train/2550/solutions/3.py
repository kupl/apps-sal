class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = [0, 0, 0]

        def give(change, amount):
            if amount == 0:
                return True

            if amount >= 20 and change[2] > 0:
                change[2] -= 1
                return give(change, amount - 20)
            elif amount >= 10 and change[1] > 0:
                change[1] -= 1
                return give(change, amount - 10)
            elif amount >= 5 and change[0] > 0:
                change[0] -= 1
                return give(change, amount - 5)
            else:
                return False

        index = {5: 0, 10: 1, 20: 2}

        for bill in bills:

            change[index[bill]] += 1

            giveBack = bill - 5

            if give(change, giveBack) == False:
                return False

        return True
