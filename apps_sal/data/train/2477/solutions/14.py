class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        haveList = list()
        ans = 0
        for i in range(len(A)):
            odd = dict()
            even = dict()
            for y,v in enumerate(A[i]):
                if y % 2 == 0:
                    odd[v] = odd.get(v,0)+1
                else:
                    even[v] = even.get(v,0)+1
            if [odd,even] not in haveList:
                haveList.append([odd,even])
        return len(haveList)
