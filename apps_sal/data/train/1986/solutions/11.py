class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        bi = str(bin(start))[2:].zfill(n)
        def get_perm(bi_start, l):
            a = bi_start[-1*l]
            b = str(1 - int(a))
            if l == 1: return [a, b]
            perms = get_perm(bi_start, l-1)
            return [a+e for e in perms] + [b+e for e in perms[::-1]]
        return list(map(lambda x: int(x, 2), get_perm(bi, len(bi))))
