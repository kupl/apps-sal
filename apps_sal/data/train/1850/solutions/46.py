class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 1:
            return [0]
        dt = {}
        for e in edges:
            if e[0] not in dt:
                dt[e[0]] = []
            dt[e[0]].append(e[1])
            if e[1] not in dt:
                dt[e[1]] = []
            dt[e[1]].append(e[0])
        sk = [0]
        st = set()
        self.tree = {}
        while sk:
            node = sk[-1]
            sk.pop()
            st.add(node)
            self.tree[node] = {'d': 0, 'n': 0, 'c': []}
            for i in dt[node]:
                if i not in st:
                    sk.append(i)
                    self.tree[node]['c'].append(i)
        self.dfs(0)
        self.help(0, self.tree[0]['d'], self.tree[0]['n'])
        ans = [0 for _ in range(N)]
        for key in self.tree:
            ans[key] = self.tree[key]['d']
        return ans

    def dfs(self, key):
        if not self.tree[key]:
            return
        dst, num = 0, 0
        for ch in self.tree[key]['c']:
            self.dfs(ch)
            dst += self.tree[ch]['d'] + self.tree[ch]['n']
            num += self.tree[ch]['n']
        self.tree[key]['d'] = dst
        self.tree[key]['n'] = num + 1

    def help(self, key, dst, num):
        if num > self.tree[key]['n']:
            self.tree[key]['d'] = dst + num - 2 * self.tree[key]['n']
            self.tree[key]['n'] = num
        for ch in self.tree[key]['c']:
            self.help(ch, self.tree[key]['d'], self.tree[key]['n'])
