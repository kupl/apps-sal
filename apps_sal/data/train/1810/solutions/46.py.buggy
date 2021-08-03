from collections import OrderedDict

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans=[]
        mem=OrderedDict()
        for i in names:
            if(i not in mem):
                ans.append(i)
                mem[i]=1
            else:
                tem=i
                count=mem[i]
                while(tem+\"(\"+str(count)+\")\" in mem):
                    count+=1
                ans.append(tem+\"(\"+str(count)+\")\")
                mem[tem]=count+1
                if(tem+\"(\"+str(count)+\")\" not in mem):
                    mem[tem+\"(\"+str(count)+\")\"]=1
            # print(mem)
        return mem.keys()
