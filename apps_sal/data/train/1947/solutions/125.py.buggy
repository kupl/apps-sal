class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        \"\"\"def checkSubset(a, B):
            aDict = {}
            bDict = {}
            for b in B:
                bSet = set(b)
                for c in bSet:
                    if b.count(c) > a.count(c):
                        return False
            return True
        ret = []
        for a in A:
            if not checkSubset(a, B):
                continue
            else:
                ret.append(a)
        return ret\"\"\"
        \"\"\"def convertB(b):
            d = {}
            for c in b: 
                if c not in d:
                    d[c] = 1
                else:
                    d[c]+=1
            return d 
        for i in range(len(B)):
            B[i] = convertB(B[i])
        def convertA(a):
            d = {}
            for c in a:
                if c not in d:
                    d[c]=1
                else:
                    d[c]+=1
            return d
        convertedA = []
        for i in range(len(A)):
            convertedA.append(convertA(A[i]))
        
        def isGoodWord(aDict):
            for wordDict in B:
                for c in wordDict:
                    if c not in aDict or wordDict[c] > aDict[c]:
                        return False
            return True
        ret = []
        for i in range(len(convertedA)):
            if isGoodWord(convertedA[i]):
                ret.append(A[i])
        return ret\"\"\"
        bDict = {}
        def convertB(b):
            d = {}
            for c in b: 
                if c not in d:
                    d[c] = 1
                else:
                    d[c]+=1
            return d 
        for i in range(len(B)):
            B[i] = convertB(B[i])
        for d in B:
            for key in d:
                if key not in bDict:
                    bDict[key] = d[key]
                else:
                    if bDict[key] < d[key]:
                        bDict[key] = d[key]
        def convertA(a):
            d = {}
            for c in a:
                if c not in d:
                    d[c]=1
                else:
                    d[c]+=1
            return d
        def isGoodWord(aDict):
            for key in bDict:
                if key not in aDict or bDict[key] > aDict[key]:
                    return False
            return True
        
        convertedA = []
        
        ret = []
        for i in range(len(A)):
            convertedA.append(convertA(A[i]))
        for i in range(len(convertedA)):
            if isGoodWord(convertedA[i]):
                ret.append(A[i])
        return ret
            
        
            
                
            
        
                
                
