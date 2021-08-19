class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjL = defaultdict(list)
        for u, v in dislikes:
            adjL[u].append(v)
            adjL[v].append(u)

        memo = [-1] * (N + 1)  # -1: not seen, 0: group 1, 1: group 2

        def df(src, shouldBe):
            if memo[src] != -1:
                return memo[src] == shouldBe
            memo[src] = shouldBe
            for dst in adjL[src]:
                if not df(dst, shouldBe ^ 1):
                    return False
            return True

        for i in range(1, N + 1):
            if memo[i] == -1 and not df(i, 0):
                return False
        return True
