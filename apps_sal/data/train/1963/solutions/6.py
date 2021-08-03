class Solution:
    def shoppingOffers(self, price, special, needs):
        a = 0
        n = len(needs)
        for i in range(n):
            a += needs[i] * price[i]

        for s in special:
            new_needs = needs.copy()
            check = True
            for i in range(n):
                new_needs[i] = new_needs[i] - s[i]
                if new_needs[i] < 0:
                    check = False
                    break

            if check:
                a = min(a, s[n] + self.shoppingOffers(price, special, new_needs))
        return a
