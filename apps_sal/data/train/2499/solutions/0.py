class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def findGCD(a, b):
            if b == 0:
                return a
            return findGCD(b, a % b)

        hash_cards = {}
        for card in deck:
            if card in hash_cards:
                hash_cards[card] += 1
            else:
                hash_cards[card] = 1
        value_ = list(hash_cards.values())
        res = value_[0]
        for x in value_[1:]:
            res = findGCD(res, x)
        if res < 2:
            return False
        return True
