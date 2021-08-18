class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        mean = arr[(len(arr) - 1) // 2]

        arr2 = list(map(lambda x: abs(x - mean), arr))
        arr3 = list(zip(arr, arr2))
        arr4 = sorted(arr3, key=lambda kv: (-kv[1], -kv[0]))

        return [arr4[i][0] for i in range(0, k)]
