class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        N = len(deck)

        if N <= 2:
            if N == 1:
                return False

            if len(set(deck)) == 1:
                return True
            else:
                return False

        cardCount = defaultdict(int)

        for card in deck:
            cardCount[card] += 1

        gcd = list(cardCount.values())[0]

        for val in list(cardCount.values())[1:]:
            gcd = math.gcd(gcd, val)

        return True if gcd >= 2 else False
