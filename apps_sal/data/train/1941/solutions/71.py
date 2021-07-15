from functools import reduce
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        # Trie
        ans = [0] * len(puzzles)
        T = lambda: collections.defaultdict(T)
        trie = T()
        for w in words:
            cur = reduce(dict.__getitem__, sorted(set(w)), trie)
            if '#' not in cur:
                cur['#'] = 1
            else:
                cur['#'] += 1
                
        def dfs(cur, i, head):
            p = puzzles[i]
            if '#' in cur and head:
                ans[i] += cur['#']
            for c in cur:
                if c in p:
                    if p[0] == c or head:
                        dfs(cur[c], i, True)
                    else:
                        dfs(cur[c], i, False)
            return
        
        for i in range(len(puzzles)):
            dfs(trie, i, False)
            
        return ans
        
        
        
        # # Using build-in combinations
        # cnt = Counter(frozenset(w) for w in words if len(set(w)) <= 7)
        # ans = []
        # for p in puzzles:
        #     cur = 0
        #     for k in range(7):
        #         for i in itertools.combinations(p[1:], k):
        #             cur += cnt[frozenset((p[0],) + i)]
        #     ans.append(cur)
        # return ans
                    
        
        # # bit-mask & bfs-based combinations
        # ans = []
        # cnt = Counter()
        # for w in words:
        #     w = set(w)
        #     if len(w) > 7:
        #         continue
        #     w_bit = 0
        #     for c in w:
        #         w_bit |= 1 << ord(c) - ord('a')
        #     cnt[w_bit] += 1
        # for p in puzzles:
        #     bfs = [1 << ord(p[0]) - ord('a')]
        #     for c in p[1:]:
        #         bfs += [m | 1 << ord(c) - ord('a') for m in bfs]
        #     ans.append(sum(cnt[m] for m in bfs))
        # return ans

