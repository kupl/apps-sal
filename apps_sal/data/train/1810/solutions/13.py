class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        m = defaultdict(int)
        ret = []
        taken = set([])
        for name in names:
            
            if name in m or name in taken:
                if name not in m:
                    m[name] = 1
                new_name = name+\"(\"+str(m[name])+\")\"
                while new_name in taken:
                    m[name]+=1
                    new_name = name+\"(\"+str(m[name])+\")\"
                ret.append(new_name)
                taken.add(new_name)
            else:
                taken.add(name)
                ret.append(name)
                m[name] = 1
                
        return ret
            
