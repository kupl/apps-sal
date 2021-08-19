class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        cards = Counter(deck)
        min_cnt = min(cards.values())
        for i in range(2, min_cnt + 1):
            divided = [v % i for v in list(cards.values())]
            if not any(divided):
                return True
        return False
