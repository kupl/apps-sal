class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        bwdict = Counter(B[0])
        for bw in B[1:]:
            tmpCounter = Counter(bw)
            for (key, val) in list(tmpCounter.items()):
                wcnt = bwdict.get(key, -1)
                if val > wcnt:
                    bwdict[key] = val
        print(bwdict)
        for word in A:
            tmpW = (word + '.')[:-1]
            wdict = Counter(word)
            isSub = []
            for (key, val) in list(bwdict.items()):
                wcnt = wdict.get(key, -1)
                if val <= wcnt:
                    isSub.append(True)
                else:
                    isSub.append(False)
            if all(isSub):
                res.append(word)
        return res
