class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # cnt = Counter(frozenset(w) for w in words if len(set(w)) <= 7)
        # ans = []
        # for p in puzzles:
        #     cur = 0
        #     for k in range(7):
        #         for i in itertools.combinations(p[1:], k):
        #             cur += cnt[frozenset((p[0],) + i)]
        #     ans.append(cur)
        # return ans
                    
        
        
        ans = []
        cnt = Counter()
        for w in words:
            w = set(w)
            if len(w) > 7:
                continue
            w_bit = 0
            for c in w:
                w_bit |= 1 << ord(c) - ord('a')
            cnt[w_bit] += 1
        for p in puzzles:
            bfs = [1 << ord(p[0]) - ord('a')]
            for c in p[1:]:
                bfs += [m | 1 << ord(c) - ord('a') for m in bfs]
            ans.append(sum(cnt[m] for m in bfs))
        return ans

