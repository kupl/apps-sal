class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for v in itertools.combinations([i for i in range(len(arr))], 3):
            if (
                abs(arr[v[0]]- arr[v[1]]) <= a and
                abs(arr[v[1]]- arr[v[2]]) <= b and
                abs(arr[v[0]]- arr[v[2]]) <= c
            ): count += 1
        return count
