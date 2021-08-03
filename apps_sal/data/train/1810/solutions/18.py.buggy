class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # Keep track of mapping from base file name (from names[i]) to current index
        # Issue with that is that the current index not be available --> instead store in list
            # Keep track of mapping from base file name (from names[i]) to current index
        # Issue with that is that the current index not be available --> instead store in list
        d = {}
        ret = [\"\" for _ in range(len(names))]
        for i, name in enumerate(names):
            if name not in d:
                ret1 = name
                num=0
            else:
                num = d[name]+1
                while name + \"(\" + str(num) + \")\" in d:
                    num += 1
                ret1 = name + \"(\" + str(num) + \")\"
                d[ret1] = 0
                
            d[name] = num
            ret[i] = ret1

            

        return ret
