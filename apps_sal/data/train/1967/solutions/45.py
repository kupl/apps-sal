class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def dfs1(prev, cur, pos):
            if pos == len(S) - 1:
                return True

            nex = prev + cur
            prev = cur
            cur = nex
            if cur > 2 ** 31 - 1:
                return False

            if S[pos + 1:pos + 1 + len(str(nex))] == str(nex):
                if len(S[pos + 1:pos + 1 + len(str(nex))]) != 1 and S[pos + 1:pos + 1 + len(str(nex))][0] == '0':
                    return False
                else:
                    return dfs1(prev, cur, pos + len(str(nex)))
            else:
                return False

        def dfs2(res, prev, cur, pos):
            res.append(prev)
            if pos == len(S) - 1:
                res.append(cur)
                return

            nex = prev + cur
            prev = cur
            cur = nex
            dfs2(res, prev, cur, pos + len(str(nex)))

        for i in range(len(S) - 1):
            for j in range(i + 1, len(S) - 1):
                if (len(S[:i + 1]) > 1 and S[:i + 1][0] == '0') or (len(S[i + 1:j + 1]) > 1 and S[i + 1:j + 1][0] == '0'):
                    continue
                if dfs1(int(S[:i + 1]), int(S[i + 1:j + 1]), j):
                    res = []
                    dfs2(res, int(S[:i + 1]), int(S[i + 1:j + 1]), j)
                    return res

        return []
