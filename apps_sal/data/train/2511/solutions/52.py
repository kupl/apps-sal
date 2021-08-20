class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        length = len(A)
        n = length // 2
        mydict = {}
        for item in A:
            mydict[item] = mydict.get(item, 0) + 1
            if mydict[item] == n:
                return item
