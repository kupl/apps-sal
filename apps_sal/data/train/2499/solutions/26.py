class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        if len(deck) <= 1:
            return False

        dict1 = {}

        for ele in deck:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1

        for i in range(2, len(deck) + 1):
            if all(v % i == 0 for v in list(dict1.values())):
                return True

        return False
