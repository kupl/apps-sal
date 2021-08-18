class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dic = {}
        type1 = 0
        type2 = 0
        type3 = 0
        for edge in edges:
            etype, a, b = edge
            if a in dic:
                if b in dic[a]:
                    dic[a][b].add(etype)
                else:
                    dic[a][b] = set([etype])
            else:
                dic[a] = {b: set([etype])}
            if b in dic:
                if a in dic[b]:
                    dic[b][a].add(etype)
                else:
                    dic[b][a] = set([etype])
            else:
                dic[b] = {a: set([etype])}
            if etype == 1:
                type1 += 1
            elif etype == 2:
                type2 += 1
            else:
                type3 += 1

        res = 0

        seen_A = [0] * n

        def dfs_A(i):
            seen_A[i - 1] = 1
            if i in dic:
                for j in dic[i]:
                    if (1 in dic[i][j] or 3 in dic[i][j]) and seen_A[j - 1] == 0:
                        dfs_A(j)
        seen_B = [0] * n

        def dfs_B(i):
            seen_B[i - 1] = 1
            if i in dic:
                for j in dic[i]:
                    if (2 in dic[i][j] or 3 in dic[i][j]) and seen_B[j - 1] == 0:
                        dfs_B(j)

        dfs_A(1)
        if sum(seen_A) != n:
            return -1
        dfs_B(1)
        if sum(seen_B) != n:
            return -1

        seen_3 = [0] * n

        def dfs_3(i):
            seen_3[i - 1] = 1
            self.cnt += 1
            if i in dic:
                for j in dic[i]:
                    if (3 in dic[i][j]) and seen_3[j - 1] == 0:
                        dfs_3(j)

        tmp = 0
        self.cnt = 0
        tmp_n = 0
        for i in range(1, n + 1):
            if seen_3[i - 1] == 0:
                tmp_n += 1
                self.cnt = 0
                dfs_3(i)
                tmp += self.cnt - 1

        res += type3 - tmp

        return res + type1 + type2 - (tmp_n - 1) - (tmp_n - 1)
