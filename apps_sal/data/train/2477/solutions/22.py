class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s = set()
        for a in A:
            s.add(''.join(sorted(a[::2])) + ''.join(sorted(a[1::2])))
        return len(s)
