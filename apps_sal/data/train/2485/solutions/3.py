class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c = 0
        if low < 0 or high > 10**9:
            return
        else:
            if (low % 2 != 0 and high % 2 != 0):
                return int((high - low) / 2) + 1
            elif ((low % 2 == 0 and high % 2 != 0) or (low % 2 != 0 and high % 2 == 0)):
                return int((high - low) / 2) + 1
            else:
                return int((high - low) / 2)
