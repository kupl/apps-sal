class Solution:
    def countGoodTriplets(self, array: List[int], a: int, b: int, c: int) -> int:
        triplets = []
        for i in range(len(array) - 2):
            for j in range(i + 1, len(array) - 1):
                for k in range(j + 1, len(array)):
                    triplets.append((array[i], array[j], array[k]))

        count = 0
        for first, second, third in triplets:
            if abs(first - second) <= a and abs(second - third) <= b and abs(first - third) <= c:
                count += 1

        return count
