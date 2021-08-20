class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        in_hand = {5: 0, 10: 0, 20: 0}
        for amount in bills:
            to_return = amount - 5
            if to_return == 15:
                if in_hand[5] and in_hand[10]:
                    in_hand[5] -= 1
                    in_hand[10] -= 1
                elif in_hand[5] >= 3:
                    in_hand[5] -= 3
                else:
                    return False
            elif to_return == 10:
                if in_hand[10]:
                    in_hand[10] -= 1
                elif in_hand[5] >= 2:
                    in_hand[5] -= 2
                else:
                    return False
            elif to_return == 5:
                if in_hand[5]:
                    in_hand[5] -= 1
                else:
                    return False
            in_hand[amount] += 1
        return True
