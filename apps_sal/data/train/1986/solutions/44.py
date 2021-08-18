class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gc = [0]
        for i in range(1, 2**n):
            gc.append(gc[-1] ^ (i & -i))

        l = len(gc)
        for i in range(l):
            fe = gc[0]
            if fe == start:
                break
            else:
                gc.append(gc.pop(0))
        return gc
