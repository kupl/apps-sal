class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = []
        decimals = set()

        for denom in range(1, n + 1):
            for num in range(1, denom + 1):
                if num % denom != 0 and num / denom not in decimals:  # we don't want whole numbers, so num % denom != 0
                    decimals.add(num / denom)
                    fractions.append(str(num) + '/' + str(denom))

        return fractions
