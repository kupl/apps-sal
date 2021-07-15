class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i, n in enumerate(arr):

            if i > len(arr) - 3:
                break

            tmp = arr[i + 1:]

            for j, m in enumerate(tmp[:-1]):
                if abs(n - m) > a:
                    continue

                for o in tmp[j + 1:]:

                    if abs(m - o) <= b and abs(n - o) <= c:
                        count += 1

        return count
