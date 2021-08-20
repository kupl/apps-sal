class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        o = []
        ptr = 0
        for n in range(1, arr[-1]):
            if ptr < len(arr) and n != arr[ptr]:
                o.append(n)
            else:
                ptr += 1
        if k > len(o):
            return arr[-1] + k - len(o)
        else:
            return o[k - 1]
