class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        com_conn = [i for i in range(n + 1)]
        size = [1 for i in range(n + 1)]
        com_count = [n]
        removed = [0]
        coed = 0
        a_edge = list()
        b_edge = list()
        for i in edges:
            if i[0] == 3:
                self.union(i[1], i[2], com_conn, com_count, removed, size)
                coed += 1
            elif i[0] == 1:
                a_edge.append(i)
            else:
                b_edge.append(i)
        if com_count[0] == 1:
            return removed[0] + len(edges) - coed

        aconn = com_conn.copy()
        asize = size.copy()
        acom_count = com_count.copy()
        for i in a_edge:
            if i[0] == 1:
                self.union(i[1], i[2], aconn, acom_count, removed, asize)
        if acom_count[0] > 1:
            return -1

        bconn = com_conn.copy()
        bsize = size.copy()
        bcom_count = com_count.copy()
        for i in b_edge:
            if i[0] == 2:
                self.union(i[1], i[2], bconn, bcom_count, removed, bsize)
        if bcom_count[0] > 1:
            return -1
        return removed[0]

    def find(self, p, connect):
        while p != connect[p]:
            p = connect[p]
        return p

    def union(self, p, q, connect, count, remove, size):
        proot = self.find(p, connect)
        qroot = self.find(q, connect)
        if proot == qroot:
            remove[0] += 1
            return
        if size[proot] > size[qroot]:
            connect[qroot] = proot
            size[proot] += size[qroot]
        else:
            connect[proot] = qroot
            size[qroot] += size[proot]
        count[0] -= 1
