class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #         mine
        #         res = collections.defaultdict(list)
        #         res_return = []
        #         for i,j in enumerate(groupSizes):
        #             res[j].append(i)

        #         for j in res:
        #             temp = [res[j][0:j]]
        #             if len(res[j])>j:
        #                 # print(j,res[j][1])
        #                 # sub_nums = int(len(res[j])/j)
        #                 for num in range(j,len(res[j]),j):
        #                     temp = temp + [res[j][num:num+j]]
        #                     # print(temp)
        #                 res[j]=temp
        #             res_return = res_return+temp
        #         # print(res)
        #         # print(res_return)
        #         return res_return

        # other perple
        groups = defaultdict(list)
        result = []
        for index, size in enumerate(groupSizes):
            groups[size].append(index)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result
