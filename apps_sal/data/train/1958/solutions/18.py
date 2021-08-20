class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = []
        subgroup = []
        count = 0
        leng = len(groupSizes)
        subsize = 0
        while count < leng:
            size = min(groupSizes)
            while size in groupSizes:
                ind = groupSizes.index(size)
                subgroup.append(ind)
                groupSizes[ind] = 501
                count += 1
                subsize += 1
                if subsize % size == 0:
                    output.append(subgroup)
                    subgroup = []
                    subsize = 0
            subgroup = []
        return output
