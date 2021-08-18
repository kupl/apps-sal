class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        d = {}
        n = len(G)
        for i in range(0, n):
            d[G[i]] = i
        fa = [i for i in range(0, n)]
        rank = [1] * n

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):

            if x == y:
                return
            else:
                i = fa[x]
                j = fa[y]
                if rank[i] <= rank[j]:
                    fa[i] = j
                else:
                    fa[j] = i
                if rank[i] == rank[j]:
                    rank[j] += 1
        p = head
        while(p and p.__next__):
            if p.val in d and p.next.val in d:

                union(d[p.val], d[p.next.val])
            p = p.__next__

        r = 0
        rset = set()

        for i in range(0, n):
            tmp = find(i)
            if tmp not in rset:
                rset.add(tmp)
                r += 1
        return r
