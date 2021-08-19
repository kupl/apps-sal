class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        med = arr[(len(arr) - 1) // 2]
        heap = []
        for a in arr:
            strength = abs(a - med)
            if len(heap) == k:
                heappushpop(heap, (strength, a))
            else:
                heappush(heap, (strength, a))
        return [a for (_, a) in heap]
