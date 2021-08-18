class Solution(object):
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        memo = {}

        def dfs(t, s, cur_stmp):
            if (t, s) in memo:
                return memo[t, s]
            if s == len(stamp):
                if t < len(target):
                    for i, ch in enumerate(stamp):
                        if ch == target[t]:
                            suffix_stmp_seq = dfs(t, i, t - i)
                            if suffix_stmp_seq:
                                memo[t, s] = suffix_stmp_seq + [cur_stmp]
                                return suffix_stmp_seq + [cur_stmp]
                    else:
                        memo[t, s] = []
                        return []
                else:
                    memo[t, s] = [cur_stmp]
                    return [cur_stmp]

            if t == len(target):
                memo[t, s] = []
                return []

            if stamp[s] == target[t]:
                seq1 = dfs(t + 1, s + 1, cur_stmp)
                if seq1:
                    memo[t, s] = seq1
                    return seq1
                else:
                    cand = dfs(t + 1, 0, t + 1)
                    memo[t, s] = [cur_stmp] + cand if cand else []
                    return [cur_stmp] + cand if cand else []

            elif stamp[s] != target[t]:
                if stamp[0] == target[t]:
                    suffix_stmp_seq = dfs(t, 0, t)
                    memo[t, s] = [cur_stmp] + dfs(t, 0, t) if suffix_stmp_seq else []
                    return [cur_stmp] + dfs(t, 0, t) if suffix_stmp_seq else []
                else:
                    memo[t, s] = []
                    return []

        return dfs(0, 0, 0)
