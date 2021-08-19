class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def dfs(curr, special, needs):
            p = curr + sum(p * needs[i] for i, p in enumerate(price))
            for si in range(len(special)):
                s = special[si]
                if all(n >= s[i] for i, n in enumerate(needs)):
                    p = min(p, dfs(curr + s[-1], special[si:], [n - s[i] for i, n in enumerate(needs)]))
                # else: p=min(p, dfs(curr, special[si+1:], needs))
            return p
        return dfs(0, special, needs)
