class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        memo, ls, lt = {}, len(stamp), len(target)
        def dfs(s, t, seqs):
            if t == lt:
                memo[s, t] = seqs if s == ls else []
            if (s, t) not in memo:
                # stamp down
                if s == ls:
                    for i in range(ls):
                        cand = dfs(i, t, [t-i]+seqs)
                        if cand:
                            memo[s, t] = cand
                            break
                    else: 
                        memo[s, t] = []
                # stamp up
                elif target[t] == stamp[s]:
                    cand = dfs(s+1, t+1, seqs)
                    memo[s, t] = cand if cand else dfs(0, t+1, seqs+[t+1])
                # no match
                else:
                    memo[s, t] = []
            return memo[s, t]
            
        return dfs(0, 0, [0])
