class Solution:

    def dfs(self, i):
        self.tmp.append(self.ls[i])
        self.idx.append(i)
        self.visited.add(i)
        for j in self.d[i]:
            if j not in self.visited:
                self.dfs(j)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.ls = list(s)
        self.visited = set()
        self.d = [[] for _ in range(len(self.ls))]
        for (i, j) in pairs:
            self.d[i].append(j)
            self.d[j].append(i)
        for i in range(len(self.ls)):
            if i not in self.visited:
                self.tmp = []
                self.idx = []
                self.dfs(i)
                sorted_tmp = sorted(self.tmp)
                sorted_idx = sorted(self.idx)
                for index in range(len(sorted_idx)):
                    self.ls[sorted_idx[index]] = sorted_tmp[index]
        return ''.join(self.ls)
