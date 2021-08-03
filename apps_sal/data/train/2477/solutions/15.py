class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set([''.join(sorted(s[0::2])) + ''.join(sorted(s[1::2])) for s in A]))
