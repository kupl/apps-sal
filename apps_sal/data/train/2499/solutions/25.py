class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        seen = {}
        for card in deck:
            if card in seen:
                seen[card] += 1
            else:
                seen[card] = 1

        for i in range(2, len(deck) + 1):
            if self.helper(seen, i):
                return True

        return False

    def helper(self, seen, val):
        for key, item in list(seen.items()):
            if item % val != 0:
                return False
        return True
