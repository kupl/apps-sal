from operator import itemgetter


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #trips = sorted(trips,key=itemgetter(2))
        dp = [0] * 1001
        for t in trips:
            for j in range(t[1], t[2]):
                dp[j] += t[0]
                # print(dp)
                if dp[j] > capacity:
                    return False

        return True
