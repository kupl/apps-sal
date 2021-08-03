class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        #
        # BFS & DP ----- Time Limit Exceeded
        # -----------------------------------------------------------------------------------------------
        # n = len(target)
        # k = len(stamp)
        # visited = set()
        # q = [(\"?\" * len(target), [])]
        # while q:
        #     cur_str, seq = q.pop(0)
        #     for i in range(0, n-k+1):
        #         new_str = cur_str[:i] + stamp + cur_str[i + k:]
        #         if new_str == target:
        #             return seq + [i]
        #         if new_str not in visited:
        #             visited.add(new_str)
        #             q.append((new_str, seq + [i]))
        # return []
    
    
        #
        # DFS & DP ----- 96 ms (94.35%) / 20.6 MB (6.00%)
        # 
        # Here are few rules for this problem:
        #
        # 1. stamp[0] has to be equal with target[0]
        # 2. stamp[-1] has to be equal with target[-1]
        # 3. We keep checking pairs of (stamp[s], target[t]). When checking (s, t). 
        #    If stamp[s] equals to target[t], we can move forward to (s+1, t+1). 
        #    Otherwise, we add a new stamp at index t+1 and stamp[0] has to be equal with target[t+1]. 
        #    Then we move forward to (0, t+1). (If stamp[0] != target[t+1] here, 
        #    there is no way to stamp without overwriting previous stamped sequence).
        # 4. When a stamp is used up, s == len(stamp), and we can try any i that stamp[i] == target[t]. 
        #    In such case, we stamp at index t-i at the beginning of the sequence so that 
        #    stamp[:i] will be overwritten by \"later\" stamps and we move forward to (i, t).
        # 5. We finish our search when we reach the end of target or t == len(target). 
        #    Based on rule #2, if i == len(stamp) as well, we have a valid sequence.
        # 
        # Based on these rules, we can build a DFS with memoization. The speed beats 90%.
        # -----------------------------------------------------------------------------------------------
        memo, ls, lt = {}, len(stamp), len(target)
        
        def dfs(s, t, seqs):
            if t == lt:
                memo[s, t] = seqs if s == ls else []
            if (s, t) not in memo:
                if s == ls:
                    for i in range(ls):
                        if stamp[i] != target[t]:
                            continue
                        cand = dfs(i, t, [t-i]+seqs)
                        if cand:
                            memo[s, t] = cand
                            break
                        else: 
                            memo[s, t] = []
                elif target[t] == stamp[s]:
                    cand = dfs(s+1, t+1, seqs)
                    memo[s, t] = cand if cand else dfs(0, t+1, seqs+[t+1])
                else:
                    memo[s, t] = []
            return memo[s, t]
        
        return dfs(0, 0, [0])
                
            
\"\"\"
Test Cases
movesToStamp(\"abc\", \"ababc\")
movesToStamp(\"ab\", \"babab\")
movesToStamp(\"o\", \"oooooooooooooooooooo\")

\"\"\"
