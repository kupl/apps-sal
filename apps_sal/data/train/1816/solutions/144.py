class Solution:
    from collections import deque
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        if not keyName:
            return []
        ret_list = []
        dict_ind = {}
        count = 0
        for nme, tme in zip(keyName,keyTime):
            if not nme in dict_ind:
                dict_ind[nme] = [(int(tme.split(\":\")[0])*60)+(int(tme.split(\":\")[1]))]
            else:
                dict_ind[nme].append((int(tme.split(\":\")[0])*60)+(int(tme.split(\":\")[1])))
        for key, val in dict_ind.items():
            if len(dict_ind[key]) >= 3 and not key in ret_list:
                val_sort = sorted(val)
                for i in range(len(val_sort)-2):
                    if val_sort[i+2]-val_sort[i] > 0:
                        if val_sort[i+2]-val_sort[i] <= 60:
                            ret_list.append(key)
                            break
                    # else:
                    #     if val[i+2]+1440-val[i] <= 60:
                    #         ret_list.append(nme)
                    #         break
                    # diff = int(dict_ind[nme][-1][0:2]) - int(dict_ind[nme][0][0:2])
                    # if diff == 0:
                    #     ret_list.append(nme)
                    # elif diff == 1:
                    #     if int(dict_ind[nme][0][3:5]) >= int(dict_ind[nme][-1][3:5]):
                    #         ret_list.append(nme)
                    #     else:
                    #         dict_ind[nme].pop(0)
        return sorted(ret_list)
