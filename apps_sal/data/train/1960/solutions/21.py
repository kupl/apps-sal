class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        a = [i for i in range(1, m + 1)]
        x = {}
        for i in range(len(a)):
            x[a[i]] = i
        b = []
        for i in queries:
            b.append(x[i])
            a = [i] + a[:x[i]] + a[x[i] + 1:]
            for j in range(x[i] + 1):
                x[a[j]] = j
        return b
