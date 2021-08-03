class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        group_dict = dict()

        for i in groupSizes:
            if i in group_dict:
                group_dict[i] += 1
            else:
                group_dict[i] = 1

        for i in group_dict.keys():
            group_dict[i] = int(group_dict[i] / i)

        group_lists = dict()

        for i in group_dict.keys():
            group_lists[i] = [[] for i in range(group_dict[i])]

        for i in range(len(groupSizes)):
            val = groupSizes[i]
            l = group_lists[val]
            j = 0
            while(len(l[j]) == val):
                j = j + 1

            l[j].append(i)

        result = []

        for i in group_lists.keys():
            result.extend(group_lists[i])

        return result
