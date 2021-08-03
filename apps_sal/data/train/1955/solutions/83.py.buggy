class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # create joined sets 
        # [0, 3] and [1, 2]
        # [0, 3, 2, 1] = \"abcd\"
        # a at position 0, b at 1 ...
        # [0 1 2 3]
        # [0 1 2 0]
        # [0 1 1 0]
        # [0 0 0 0]
        # let the value at the index represent it's parent
        # Create a set
        parentList = [i for i in range(len(s))]
        # letterList = [[] for i in range(len(s))]
        def setRoot(parent, child):
            if parentList[parent] == child or parentList[child] == parent:
                return
            if parentList[parent] > parentList[child]:
                return setRoot(child, parent)
            if parent == child:
                return
            childParent = parentList[child]
            parentList[child] = parent
            setRoot(parent, childParent)
            
        def findParent(child, i):
            # if i == 0:
                # print(child)
            parent = parentList[child]
            if child != parentList[child]:
                parent = findParent(parentList[child], i+1)
                parentList[child] = parent
            return parent
            
        for pair in pairs:
            # print(parentList)
            # if parentList[pair[0]] < parentList[pair[1]]:
            setRoot(pair[0], pair[1])
            # else:
            #     setRoot(pair[1], pair[0])
        letterSets = {}
        
        # print(parentList)
        for i in range(len(s)):
            l = s[i]
            parent = findParent(i, 0)
            
            entry = letterSets.get(parent, [[], []])
            entry[0].append(l)
            entry[1].append(i)
            letterSets[parent] = entry
        retList = ['a' for i in range(len(s))]
        for _, entry in letterSets.items():
            entry[0].sort()
            entry[1].sort()
            for i in range(len(entry[1])):
                retList[entry[1][i]] = entry[0][i]
        return \"\".join(retList)
            
            
