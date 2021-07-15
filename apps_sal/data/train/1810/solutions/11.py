class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
\t\t# Edge case: names is empty.
        if not names:
            return []
        
        assignedNames = set()
        uniqueNames = []
        
        for name in names:
            if name in assignedNames:
                k = 1
                numberedName = f'{name}({k})'
                
                while numberedName in assignedNames:
                    k += 1
                    numberedName = f'{name}({k})'
                
                assignedNames.add(numberedName)
                uniqueNames.append(numberedName)
            else:
                assignedNames.add(name)
                uniqueNames.append(name)
            
        return uniqueNames
