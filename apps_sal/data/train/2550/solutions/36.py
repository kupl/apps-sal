class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket = {5: 0, 10: 0, 20: 0}
        for x in bills:
            if x == 5:
                pocket[x] += 1
            else:
                back = x - 5
                for k in [10, 5]:
                    if back > 0 and pocket[k] > 0:
                        deduct = min(pocket[k], back // k)
                        back -= k * deduct
                        pocket[k] -= deduct
                pocket[x] += 1
                if back > 0:
                    return False
        return True
