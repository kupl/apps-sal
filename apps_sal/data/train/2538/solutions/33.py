class Solution:

    def countLargestGroup(self, n: int) -> int:
        d = {}
        for num in range(1, n + 1):
            sumn = 0
            for char in str(num):
                sumn += int(char)
            d[sumn] = d[sumn] + [num] if sumn in d else [num]
        t = {}
        for arr in d.values():
            t[len(arr)] = t[len(arr)] + 1 if len(arr) in t else 1
        tt = sorted(t, reverse=True)
        return t[next(iter(tt))]
