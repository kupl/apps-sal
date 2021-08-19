class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)  # panjang dari array
        goodTriplet = 0  # jumlah goodTriplet

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):

                    cond_1 = abs(arr[i] - arr[j]) <= a
                    cond_2 = abs(arr[j] - arr[k]) <= b
                    cond_3 = abs(arr[i] - arr[k]) <= c

                    if all([cond_1, cond_2, cond_3]):
                        goodTriplet += 1
        return goodTriplet
