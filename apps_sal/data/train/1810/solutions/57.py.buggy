from collections import defaultdict

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        store=set()
        ans=[]
        mem=defaultdict(int)
        for i in names:
            if(i not in store):
                store.add(i)
                ans.append(i)
                mem[i]=1
            else:
                tem=i
                count=mem[i]
                while(tem+\"(\"+str(count)+\")\" in store):
                    count+=1
                store.add(tem+\"(\"+str(count)+\")\")
                ans.append(tem+\"(\"+str(count)+\")\")
                mem[tem]=count+1
                if(tem+\"(\"+str(count)+\")\" not in mem):
                    mem[tem+\"(\"+str(count)+\")\"]=1
            # print(mem)
        return ans
