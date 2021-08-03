class Solution:
    def add_edge(self, parent, cnt, x, y):
        xx = self.parents(parent, x)
        yy = self.parents(parent, y)
        if(cnt[xx] < cnt[yy]):
            parent[xx] = yy
            cnt[yy] += 1
        else:
            parent[yy] = xx
            cnt[xx] += 1

    def parents(self, parent, ch):
        if(parent[ch] == ch):
            return ch
        else:
            xy = self.parents(parent, parent[ch])
            parent[ch] = xy
            return xy

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = (n + 1) * [0]
        ans = 0
        cnt = (n + 1) * [0]
        for i in range(n + 1):
            parent[i] = i
        edges.sort(reverse=True)
        for j in range(len(edges)):
            i = edges[j]
            if(i[0] != 3):
                break
            if(self.parents(parent, i[1]) != self.parents(parent, i[2])):
                self.add_edge(parent, cnt, i[1], i[2])
            else:
                ans += 1
        bob = parent.copy()
        bob_cnt = cnt.copy()
        for k in range(j, len(edges)):
            i = edges[k]
            if(i[0] != 2):
                break
            if(self.parents(bob, i[1]) != self.parents(bob, i[2])):
                self.add_edge(bob, bob_cnt, i[1], i[2])
            else:
                ans += 1
        for l in range(k, len(edges)):
            i = edges[l]
            if(i[0] != 1):
                break
            if(self.parents(parent, i[1]) != self.parents(parent, i[2])):
                self.add_edge(parent, cnt, i[1], i[2])
            else:
                ans += 1
        rn = 0
        for i in range(1, n + 1):
            if(parent[i] == i):
                rn += 1
        if(rn > 1):
            return -1
        rn = 0
        for i in range(1, n + 1):
            if(bob[i] == i):
                rn += 1
        if(rn > 1):
            return -1
        return ans
