class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        iterator = range(len(arr))
        goodies = 0
        for i in iterator:
            for j in iterator[i + 1:]:
                if abs(arr[i] - arr[j]) <= a:
                    for k in iterator[j + 1:]:
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            goodies += 1
        return goodies
