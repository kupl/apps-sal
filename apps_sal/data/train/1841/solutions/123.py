class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sort = sorted(arr)
        m = sort[int((len(arr) - 1) / 2)]

        sort.reverse()
        sorted_by_m = sorted(sort, key=lambda x: abs(x - m), reverse=True)
        print(m, sorted_by_m)
        return sorted_by_m[:k]
