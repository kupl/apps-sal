class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        h=collections.defaultdict(int)
        ans=[]
        for i in names:
            if i not in h:
                h[i]=0
                ans.append(i)
            else:
                s=i
                while s in h:
                    h[i]+=1
                    s=i + \"(\" + str(h[i]) + \")\"
                h[s]=0
                ans.append(s)
                    
                                    
        return ans       
    
    
#     seen = {}
# \t\tres = []
# \t\tfor i in names:
# \t\t\tif i not in seen:
# \t\t\t\tseen[i] = 0
# \t\t\t\tres.append(i)
# \t\t\telse:
# \t\t\t\ts = i
# \t\t\t\twhile s in seen:
# \t\t\t\t\tseen[i] += 1
# \t\t\t\t\ts = i + \"(\" + str(seen[i]) + \")\"
# \t\t\t\tseen[s] = 0
# \t\t\t\tres.append(s)
# \t\treturn res
                
