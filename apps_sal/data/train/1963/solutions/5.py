class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        res = 0
        for pric, need in zip(price, needs):
            res += pric * need
        for offer in special:
            clone = list(needs)
            i = 0
            while (i < len(needs)):
                diff = clone[i] - offer[i]
                if diff < 0:
                    break
                clone[i] = diff
                i += 1
            if i == len(needs):
                res = min(res, offer[-1] + self.shoppingOffers(price, special, clone))
        return res
