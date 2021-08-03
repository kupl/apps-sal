class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = [i for i in range(n)]

        def find(u):
            if A[u] != u:
                A[u] = find(A[u])
            return A[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            A[max(pu, pv)] = min(pu, pv)
            return True

        # 先做Common的遍历
        edges = sorted(edges, reverse=True)
        # print(\"看看顺序对不对\", edges)

        i = 0
        m = len(edges)
        res = 0
        while i < m:
            cur = edges[i]
            if cur[0] == 3:
                # 从0开始编号
                if union(cur[1] - 1, cur[2] - 1) == False:
                    res += 1
            else:
                break
            i += 1
        # print(\"common res\", res)

        # 找Bob的
        origin_A = deepcopy(A)
        while i < m:
            cur = edges[i]
            if cur[0] == 2:
                # 从0开始编号
                if union(cur[1] - 1, cur[2] - 1) == False:
                    res += 1
            else:
                break
            i += 1
        # print(\"Bob and Common\", res, A)
        for j in range(1, n):
            # 查看是否所有的节点都能够到0
            # print(j)
            p = find(j)
            if p != 0:
                # print(\"Bob \" + str(j) + \" can't to 0, only to \" + str(p))
                return -1

        # Alice
        A = origin_A
        while i < m:
            cur = edges[i]
            if cur[0] == 1:
                # 从0开始编号
                if union(cur[1] - 1, cur[2] - 1) == False:
                    res += 1
            else:
                break
            i += 1

        # print(\"Alice and Common\", A)
        for j in range(1, n):
            # 查看是否所有的节点都能够到0
            p = find(j)
            if p != 0:
                # print(\"Alice \" + str(j) + \" can't to 0, only to \" + str(p))
                return -1

        return res
