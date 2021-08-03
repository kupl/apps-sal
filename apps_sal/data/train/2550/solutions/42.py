class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5: 0, 10: 0, 20: 0}

        for x in bills:
            if x == 20:
                if (coins[10]):
                    coins[10] -= 1
                    coins[5] -= 1
                else:
                    coins[5] -= 3

                if coins[10] < 0 or coins[5] < 0:
                    return False
            elif x == 10:
                coins[5] -= 1

                if coins[5] < 0:
                    return False

            coins[x] += 1
        return True
