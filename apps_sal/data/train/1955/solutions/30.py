class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.p = [i for i in range(n)]
        for (x, y) in pairs:
            self.union(x, y)
        dic = collections.defaultdict(list)
        for i in range(n):
            dic[self.find(i)].append(s[i])
        for k in dic.keys():
            dic[k] = sorted(dic[k])
        res = []
        for i in range(n):
            res.append(dic[self.find(i)].pop(0))
        return ''.join(res)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
