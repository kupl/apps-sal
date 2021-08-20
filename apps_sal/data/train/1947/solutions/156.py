class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ret = []
        bdict = dict()
        for word in B:
            temp = collections.Counter(word)
            for (let, val) in temp.items():
                if let not in bdict:
                    bdict[let] = val
                else:
                    bdict[let] = max(bdict[let], val)
        for item in A:
            tempdict = collections.Counter(item)
            failed = False
            for (let, val) in bdict.items():
                if let not in tempdict:
                    failed = True
                    break
                elif tempdict[let] < val:
                    failed = True
                    break
            if not failed:
                ret.append(item)
        return ret
