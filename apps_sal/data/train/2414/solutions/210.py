class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        triplets = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    triplets.append([arr[i], arr[j], arr[k]])
        count = 0
        for i in triplets:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and (abs(i[0] - i[2]) <= c):
                count += 1
        return count
