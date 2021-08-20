class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = defaultdict(int)
        for i in B:
            for j in set(i):
                d[j] = max(i.count(j), d[j])
        l = []
        for i in A:
            if all((d[j] <= i.count(j) for j in list(d.keys()))):
                l.append(i)
        return l
