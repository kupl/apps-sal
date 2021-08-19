class Solution(object):

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        memo = {}
        (T, S) = (len(target), len(stamp))

        def dfs(t, s, cur_stmp):
            if t == T:
                memo[t, s] = cur_stmp if s == S else []
                return memo[t, s]
            if (t, s) not in memo:
                if s == S:
                    for i in range(S):
                        if stamp[i] == target[t]:
                            suff_stmp = dfs(t, i, [t - i])
                            if suff_stmp:
                                memo[t, s] = suff_stmp + cur_stmp
                                break
                    else:
                        memo[t, s] = []
                elif stamp[s] == target[t]:
                    suff_stmp = dfs(t + 1, s + 1, cur_stmp)
                    if suff_stmp:
                        memo[t, s] = suff_stmp
                    else:
                        suff_stmp = dfs(t + 1, 0, [t + 1])
                        memo[t, s] = cur_stmp + suff_stmp if suff_stmp else []
                elif stamp[s] != target[t]:
                    if stamp[0] == target[t]:
                        suff_stmp = dfs(t, 0, [t])
                        memo[t, s] = cur_stmp + suff_stmp if suff_stmp else []
                    else:
                        memo[t, s] = []
                return memo[t, s] if memo[t, s] else []
        return dfs(0, 0, [0])
