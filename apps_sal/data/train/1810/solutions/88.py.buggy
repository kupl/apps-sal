def assignName(name, nameLookup, assignedNames):
    baseName = name
    i = 1
    if name in assignedNames:
        i = assignedNames[name]
    while name in nameLookup:
        name = baseName + \"(\" + str(i) + \")\"
        i += 1
    nameLookup.add(name)
    assignedNames[baseName] += 1
    return name
        

    
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nameLookup = set()
        assignedNames = defaultdict(lambda:0)
        return [assignName(name, nameLookup, assignedNames) for name in names]
         
        
