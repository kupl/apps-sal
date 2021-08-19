from collections import defaultdict, Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        rd = defaultdict(int)
        for c in map(Counter, B):
            for i in c:
                rd[i] = max(rd[i], c[i])

        # b = \"\".join([i * rd[i] for i in rd])

        cts = {i: Counter(i) for i in A}
        for i in rd:
            rdi = rd[i]
            rm = set()
            for c in cts:
                if i not in cts[c] or cts[c][i] < rdi:
                    rm.add(c)
            for r in rm:
                cts.pop(r)
        return cts
