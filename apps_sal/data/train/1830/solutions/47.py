class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        return_arr = [-1 for i in range(len(rains))]
        rains_dict = {}
        zeros_indices = []
        for i in range(len(rains)):
            if(rains[i]) == 0:
                return_arr[i] = 1
                zeros_indices.append(i)
            elif rains[i] not in rains_dict:
                rains_dict[rains[i]] = i
            else:
                if len(zeros_indices) == 0:
                    return []

                index = 0
                while(zeros_indices[index] < rains_dict[rains[i]]):
                    index += 1
                    print(index)
                    if(index == len(zeros_indices)):
                        return []
                return_arr[zeros_indices[index]] = rains[i]
                rains_dict[rains[i]] = i
                del zeros_indices[index]
        return return_arr
