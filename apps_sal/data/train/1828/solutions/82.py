class Solution:
    def rearrangeBarcodes(self, a: List[int]) -> List[int]:
        count = collections.Counter(a)
        a.sort(key=lambda x: (count[x], x))
        a[1::2], a[::2] = a[:len(a) // 2], a[len(a) // 2:]
        return a
