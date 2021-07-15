from collections import defaultdict
class UnionFind:
    def __init__(self, iterable=None):
        \"\"\"初始化父子关系映射。若指定iterable，则初始化其自身\"\"\"
        self.cnt = defaultdict(lambda: 1)
        self.f = {}
        for a in iterable or []:
            self.f[a] = a
            self.cnt[a] = 1

    def size(self, a=None):
        \"\"\"返回a集合大小。若不指定a，则返回集合的个数\"\"\"
        if a is not None:
            return self.cnt[self.find(a)]
        else:
            return sum(a == self.f[a] for a in self.f)

    def same(self, a, b):
        \"\"\"判断a,b是否同一集合\"\"\"
        return self.find(a) == self.find(b)

    def find(self, a):
        \"\"\"查找a的根\"\"\"
        if self.f.get(a, a) == a:
            self.f[a] = a
            return a
        self.f[a] = self.find(self.f[a])
        return self.f[a]

    def merge(self, a, b):
        \"\"\"合并a到b的集合\"\"\"
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.f[ra] = rb
            self.cnt[rb] += self.cnt[ra]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        un = UnionFind(range(1, n+1))
        ans = 0
        for t, a, b in edges:
            if t == 3:
                if un.same(a, b):
                    ans += 1
                else:
                    un.merge(a, b)

        un1 = deepcopy(un)
        for t, a, b in edges:
            if t == 1:
                if un1.same(a, b):
                    ans += 1
                else:
                    un1.merge(a, b)

        un2 = deepcopy(un)
        for t, a, b in edges:
            if t == 2:
                if un2.same(a, b):
                    ans += 1
                else:
                    un2.merge(a, b)
        
        return ans if un1.size() == un2.size() == 1 else -1
