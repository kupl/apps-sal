class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        return self.count_profit(prices, 0, n - 1)

    def count_profit(self, prices, left, right):
        if left >= right:
            return 0
        if right - left == 1:
            profit = prices[right] - prices[left]
            if profit < 0:
                profit = 0
            return profit
        mid = (left + right) // 2
        pro_left = self.count_profit(prices, left, mid)
        pro_right = self.count_profit(prices, mid + 1, right)
        pro_mid = 0
        i = min(prices[left:mid + 1])
        j = max(prices[mid + 1:right + 1])
        pro_mid = j - i
        profit = max(pro_left, pro_mid, pro_right)
        if profit < 0:
            profit = 0
        return profit
