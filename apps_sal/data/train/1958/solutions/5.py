class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_sizes_dict = {}
        ret_groups = []
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in group_sizes_dict:
                group_sizes_dict[groupSizes[i]] = [i]
            else:
                group_sizes_dict[groupSizes[i]].append(i)
                       
        keys = sorted(group_sizes_dict.keys())
        
        for i in keys:
            tmp_list = group_sizes_dict[i]
            print(tmp_list)
            to_add = []
            
            for j in range(len(tmp_list)):
                if (j+1) % i == 0:
                    to_add.append(tmp_list[j])
                    ret_groups.append(to_add)
                    to_add = []
                else:
                    to_add.append(tmp_list[j])
                    
                
        return ret_groups

