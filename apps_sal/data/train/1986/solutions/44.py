class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gc = [0]
        for i in range(1,2**n):
            gc.append(gc[-1] ^ (i & -i)) # -i is similar to two component https://leetcode.com/problems/gray-code/discuss/245076/4-lines-Elegant-fast-and-easy-understand-Python-solution/688127 and https://stackoverflow.com/a/12250963/8006144
            
        l = len(gc)
        for i in range(l):
            fe = gc[0]
            if fe == start:
                break
            else:
                gc.append(gc.pop(0))
        return gc

