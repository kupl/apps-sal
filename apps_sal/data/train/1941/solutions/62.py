from collections import defaultdict


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        d = defaultdict(int)
        for word in words:
            wl = list(set(list(word)))
            wl.sort()
            d[''.join(wl)] += 1
        ans = []

        for puzzle in puzzles:
            f = puzzle[0]
            pl = sorted(list(puzzle))
            fi = pl.index(f)
            tmp = 0
            for i in range(2 ** (len(pl) - 1)):
                cand = []
                for j in range(len(pl)):
                    if j < fi:
                        if i & (1 << j):
                            cand.append(pl[j])
                    elif j == fi:
                        cand.append(f)
                    else:
                        if i & (1 << (j - 1)):
                            cand.append(pl[j])
                cs = ''.join(cand)
                tmp += d[cs]
            ans.append(tmp)

        return ans
