class Solution:
    def peopleIndexes(self, fc: List[List[str]]) -> List[int]:
        def helper(s, b):
            return len(set(s).intersection(set(b))) == len(s)

        n = len(fc)
        out = []
        for i in range(n):
            f = fc.pop(0)
            for rest in fc:
                if helper(f, rest):
                    out.append(i)
                    break
            fc.append(f)

        return sorted(list(set(range(n)).difference(set(out))))
