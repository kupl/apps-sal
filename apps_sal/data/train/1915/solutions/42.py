class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stampList = list(stamp)
        targetList = list(target)
        
        result = []
        changed = True
        while changed:
            changed = False
            for i in range(len(targetList) - len(stampList) + 1):
                temp = self.validTarget(stampList, targetList, i)
                
                if temp:
                    changed = True
                    result += [i]
            
            if not changed:
                break
        
        if targetList == [\"?\"] * len(targetList):
            return reversed(result)
        else:
            return []
        
        
    def validTarget(self, stamp, target, i):
        
        changed = False
        
        for j in range(len(stamp)):
            
            if target[j+i] == \"?\":
                continue
            if stamp[j] != target[i+j]:
                return False
            
            changed = True
        
        if not changed:
            return False
        
        for j in range(len(stamp)):
            target[j+i] = \"?\"
        
        return True
