class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        result = []
        seen = defaultdict(int)
        
        for n in names:
            if n not in result:
                result.append(n)
                seen[n] += 1
            else:
                count = seen[n]
                newName = \"{}({})\".format(n, count)
                
                while newName in seen:
                    count += 1
                    newName = \"{}({})\".format(n, count)
                
                result.append(newName)
                seen[newName] += 1
                seen[n] += 1
                
        return result
            
            
