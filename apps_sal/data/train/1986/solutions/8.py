class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gc, bit = [0, 1], 1
        while bit < n:
            bit += 1

            next_vals = []
            for val in reversed(gc):
                next_vals.append( val + 2**(bit-1) )
            gc.extend(next_vals)

        ind = gc.index(start)
        return gc[ind:] + gc[:ind]
