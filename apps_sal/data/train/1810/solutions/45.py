class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        s = set()
        ans = []
        d = {}
        
        for x in names:
            if x not in d:
                d[x] = 1
                ans.append(x)
                s.add(x)
            else:
                #c = d[x]
                tmp = x + \"(\" + str(d[x]) +\")\"
                #print(tmp)
                while tmp in s:
                    d[x] +=1
                    tmp = x + \"(\" + str(d[x]) +\")\"
                #print(tmp)
                d[tmp] = 1
                s.add(tmp)
                ans.append(tmp)
            #print(d)
        #print(d)
        #print(s)
        return ans
                    
        
