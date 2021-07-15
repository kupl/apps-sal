class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {20: 0,
                10: 0,
                 5: 0}
        for paid in bills:
            refund = paid - 5
            if refund == 0:
                cash[5] += 1
                continue
            flag = False
            for note in cash:
                if cash[note]>= refund//note:
                    cash[note] -= refund // note
                    refund -= (refund// note) *note
                    flag = True
            if not flag or refund>0:
                return False
            cash[paid] += 1
        return True

