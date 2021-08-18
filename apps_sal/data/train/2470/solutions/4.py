class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0

        mydict = {}
        for dom in dominoes:
            if ''.join(str(dom)) in mydict:
                mydict[''.join(str(dom))] += 1
            elif ''.join(str(dom[::-1])) in mydict:
                mydict[''.join(str(dom[::-1]))] += 1
            else:
                mydict[''.join(str(dom))] = 1
        for val in list(mydict.values()):
            if val > 1:
                count += val * (val - 1) // 2

        return count
