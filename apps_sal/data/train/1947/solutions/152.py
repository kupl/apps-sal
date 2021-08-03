class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dict2 = {}
        for i2 in B:
            dict3 = {}
            for l in i2:
                if l in dict3.keys():
                    dict3[l] += 1
                else:
                    dict3[l] = 1
                if l not in dict2.keys():
                    dict2[l] = 0
                if dict3[l] > dict2[l]:
                    dict2[l] = dict3[l]
        result = []
        for i in A:
            dict1 = {}
            is_subset = True
            for l1 in i:
                if l1 in dict1.keys():
                    dict1[l1] += 1
                else:
                    dict1[l1] = 1
            for key in dict2.keys():
                if key in dict1.keys():
                    if dict1[key] < dict2[key]:
                        is_subset = False
                else:
                    is_subset = False
            if is_subset:
                result.append(i)
        return result
