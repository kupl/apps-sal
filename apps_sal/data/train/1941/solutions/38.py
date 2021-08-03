class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cc = collections.Counter()
        for w in words:
            cc[tuple(sorted(set(list(w))))] += 1

        res = []
        for pzl in puzzles:
            possible_sets = [set([pzl[0]])]
            for i in range(1, 7):
                possible_sets.extend([st.union([pzl[i]]) for st in possible_sets])
            nvalid = sum(cc[tuple(sorted(st))] for st in possible_sets)
            res.append(nvalid)
        return res
