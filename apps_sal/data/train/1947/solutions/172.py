class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bdict = dict()
        for word in B:
            temp = collections.Counter(word)
            for let, val in temp.items():
                if let not in bdict:
                    bdict[let] = val
                else:
                    bdict[let] = max(bdict[let], val)

        i = 0
        while i < len(A):
            tempdict = collections.Counter(A[i])
            failed = False
            for let, val in bdict.items():
                if let not in tempdict:
                    failed = True
                    break
                elif tempdict[let] < val:
                    failed = True
                    break

            if failed:
                del A[i]
            else:
                i = i + 1

        return A
