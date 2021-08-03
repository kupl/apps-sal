class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        haveList = list()
        ans = 0
        for i in A:
            odd = dict()
            even = dict()
            for s in i[0::2]:
                odd[s] = odd.get(s, 0) + 1
            for s2 in i[1::2]:
                even[s2] = even.get(s2, 0) + 1
            if [odd, even] not in haveList:
                haveList.append([odd, even])
        length = len(haveList)
        return length
