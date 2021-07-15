class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        Acount = {word: collections.Counter(word) for word in A}
        Bcount = defaultdict(int)
        for b in B:
            b = collections.Counter(b)
            for k, v in b.items():
                Bcount[k] = max(Bcount[k], v)
        res = []
        for word in A:
            wCount = Acount[word]
            isWord = True
            for k, v in Bcount.items():
                if k in wCount and wCount[k] >= v:
                    continue
                else:
                    isWord = False
                    break
            if isWord:
                res.append(word)
        return res
