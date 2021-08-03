class Solution:
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        result = []
        nameset = set()
        for name in names:
            # if match := re.fullmatch(r\"(.*)\\((\\d+)\\)\", name):
            #     num = int(match.group(1))
            if name in nameset:
                candidates = (f\"{name}({num})\" for num in itertools.count(1))
                name = next(newname for newname in candidates if newname not in nameset)
            result.append(name)
            nameset.add(name)
        return result
            
            
                
