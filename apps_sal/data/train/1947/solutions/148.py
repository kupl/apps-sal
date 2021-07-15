class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        d = collections.defaultdict(int)
        for b in B:
            b = collections.Counter(b)
            for x in b:
                if b[x] > d[x]:
                    d[x] += b[x] - d[x]
        uni = []
        for a in A:
            c = collections.Counter(a)
            for i, n in list(d.items()):
                if i not in c or c[i] < n:
                    break
            else:
                uni.append(a)
        return uni

