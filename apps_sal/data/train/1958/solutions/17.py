class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ret_lst = []
        for iGrpSize in range(len(groupSizes), 0, -1):
            if iGrpSize in groupSizes:
                ppl = []
                for i in range(len(groupSizes)):
                    if groupSizes[i] == iGrpSize:
                        ppl.append(i)
                if len(ppl) > iGrpSize:
                    for i in range(0, len(ppl), iGrpSize):
                        ret_lst.append(ppl[i:i + iGrpSize])
                else:
                    ret_lst.append(ppl)
        return ret_lst
