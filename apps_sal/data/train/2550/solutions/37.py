class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        (counter, counter1, counter2, i) = (0, 0, 0, 0)
        wallet = {5: 0, 10: 0, 20: 0}
        while i < len(bills):
            if bills[i] == 5:
                counter += 1
                wallet[5] = counter
            elif bills[i] == 10:
                counter -= 1
                wallet[5] = counter
                counter1 += 1
                wallet[10] = counter1
                if counter < 0:
                    return False
            elif bills[i] == 20:
                if counter >= 1 and counter1 >= 1:
                    counter -= 1
                    wallet[5] = counter
                    counter1 -= 1
                    wallet[10] = counter1
                    counter2 += 1
                    wallet[20] = counter2
                elif counter >= 3:
                    counter -= 3
                    wallet[5] = counter
                    counter2 += 1
                    wallet[20] = counter2
                else:
                    return False
            if counter < 0 or counter1 < 0:
                return False
            i += 1
        return True
