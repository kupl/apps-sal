class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        m = arr[(len(arr) - 1) // 2]
        power = [abs(x - m) for x in arr]
        order = sorted(zip(power, arr), reverse=True)
        return [order[i][1] for i in range(k)]
