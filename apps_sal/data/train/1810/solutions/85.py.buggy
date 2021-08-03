class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        
        diction = defaultdict(int)
        seen = {}
        res = []
        for name in names:
            diction[name] += 1
            if name not in seen:
                seen[name] = True
                res.append(name)
            elif name in seen and diction[name] == 1:
                n = diction[name]
                while name+\"(\"+str(n)+\")\" in seen:
                    n += 1
                seen[name+\"(\"+str(n)+\")\"] = True
                res.append(name+\"(\"+str(n)+\")\")                
            elif name in seen and diction[name] > 1:
                n = diction[name]
                while name+\"(\"+str(n-1)+\")\" in seen:
                    n += 1
                seen[name+\"(\"+str(n-1)+\")\"] = True
                res.append(name+\"(\"+str(n-1)+\")\")
 
        #print(res)   
        return res
