class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        type1 = [[i - 1, j - 1] for t, i, j in edges if t == 1]
        type2 = [[i - 1, j - 1] for t, i, j in edges if t == 2]
        type3 = [[i - 1, j - 1] for t, i, j in edges if t == 3]

        def helper(type1, other, fa, c=False):
            def getfa(i):
                if fa[i] != i:
                    fa[i] = getfa(fa[i])
                return fa[i]
            connect_count = 0
            ret = len(other)
            for i, j in type1:
                if getfa(i) != getfa(j):
                    fa[getfa(i)] = getfa(j)
                    connect_count += 1
            for i, j in other:
                if getfa(i) != getfa(j):
                    fa[getfa(i)] = getfa(j)
                    connect_count += 1
                    ret -= 1
            # print(fa, connect_count, ret)
            if c == True or connect_count == len(fa) - 1:
                return ret
            return -1

        t1_count = helper(type3, type1, list(range(n)))
        if t1_count < 0:
            return -1
        t2_count = helper(type3, type2, list(range(n)))
        if t2_count < 0:
            return -1
        t3_count = helper([], type3, {i: i for i in set([x for x, y in type3] + [y for x, y in type3])}, True)
        return t1_count + t2_count + t3_count
