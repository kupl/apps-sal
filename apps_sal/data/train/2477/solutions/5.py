class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = []
        for s in A:
            info = len(s), Counter(s[::2]), Counter(s[1::2])
            if info not in groups:
                groups.append(info)
        return len(groups)

