class Solution:

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        def directPurchase(price, needs):
            total = 0
            for i in range(len(needs)):
                total += price[i] * needs[i]
            return total

        def dfs(price, special, needs, index):
            local_min = directPurchase(price, needs)
            for i in range(index, len(special)):
                offer = special[i]
                temp = []
                for j in range(len(needs)):
                    if needs[j] < offer[j]:
                        temp = []
                        break
                    else:
                        temp.append(needs[j] - offer[j])
                if temp != []:
                    local_min = min(local_min, offer[-1] + dfs(price, special, temp, i))
            return local_min
        return dfs(price, special, needs, 0)
