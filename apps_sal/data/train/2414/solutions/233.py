class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        x = list(range(len(arr)))
        score = 0
        for i in x:
            for j in x[i + 1:]:
                if abs(arr[i] - arr[j]) <= a:
                    for k in x[j + 1:]:
                        if (abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c):
                            score += 1
        return score
