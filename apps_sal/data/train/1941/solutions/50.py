class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
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
            bfs = [1 << (ord(p[0]) - ord('a'))]
            for c in p[1:]:
                bfs += [m | 1 << (ord(c) - ord('a')) for m in bfs]
            ans.append(sum(cnt[m] for m in bfs))
        return ans
        #     cur = 0
        #     p_bit = 0
        #     for c in p:
        #         p_bit |= 1 << ord(c) - ord('a')
        #     a = 1 << ord(p[0]) - ord('a')
        #     for w in cnt:
        #         if a & w and w & p_bit == w:
        #             cur += cnt[w]
        #     ans.append(cur)
        # return ans

