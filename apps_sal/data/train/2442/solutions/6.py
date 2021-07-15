class Solution:
    collections.OrderedDict
    def sortString(self, s: str) -> str:
        list_s = list(s)
        list_s.sort()
        dict_s = {}
        for i in range(len(list_s)):
            if list_s[i] not in dict_s:
                dict_s[list_s[i]] = 1
            else:
                dict_s[list_s[i]] += 1
        result = []
        while dict_s != {}:
            i = 0
            while dict_s != {} and i < len(dict_s):
                result.append(list(dict_s)[i])
                if dict_s[list(dict_s)[i]] - 1 == 0:
                    del dict_s[list(dict_s)[i]]
                else:
                    dict_s[list(dict_s)[i]] -= 1
                    i += 1
            i = len(dict_s) - 1
            while dict_s != {} and i >= 0:
                result.append(list(dict_s)[i])
                if dict_s[list(dict_s)[i]] - 1 == 0:
                    del dict_s[list(dict_s)[i]]
                else:
                    dict_s[list(dict_s)[i]] -= 1
                i -= 1
        return ''.join(result)
        
        

