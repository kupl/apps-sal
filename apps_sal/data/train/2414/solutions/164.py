class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i = 0
        ans = 0

        def tripleIsGood(i, j, k):
            if 0 <= i < j < k and abs(arr[i]- arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                return True

        for i in range(0, len(arr)-2):
            k = len(arr)-1

            while i + 1 != k:
            # for k in range(k, i+2, -1):
                if i+1 != k:

                    for j in range(i+1, k):

                        if tripleIsGood(i, j, k):
                            ans += 1

                k -= 1

        return ans
