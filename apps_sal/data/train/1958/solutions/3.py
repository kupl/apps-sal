class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        
        # imput: [3,3,3,3,3,3,1]
        # output: [[0,1,2],[3,4,5],[6]]

        def group_by_size(size_list: List[int]) -> List[List[int]]: # [3,3,3,3,3,3,1]
            if size_list == []:
                return []
            if size_list is None:
                raise ValueError(\"bad input..\")
            ans_list, count_dict = [], {} #  [[0, 1, 2], ], {}
            for i, num in enumerate(size_list):
                if num == 0:
                    raise ValueError(\"group size has to be larger then 0\")
                if not num in count_dict:
                    count_dict[num] = [i]
                else:
                    count_dict[num].append(i)
                if len(count_dict[num]) == num:
                    ans_list.append(count_dict[num])
                    del count_dict[num]
            if len(count_dict) > 0:
                raise ValueError(\"some elements have bad values\")
            return ans_list
        
        return group_by_size(groupSizes)
            
        
