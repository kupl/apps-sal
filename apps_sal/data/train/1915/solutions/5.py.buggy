class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        def canStamp(targetStr, idx, stamp):
            hasOneChar = False
            for i in range(len(stamp)):
                if targetStr[idx+i] == \"?\":
                    continue
                
                if targetStr[idx+i] == stamp[i]:
                    hasOneChar = True
                    continue
                else:
                    return False
            if hasOneChar:
                return True
            else:
                return False
            
        
        queue = [(target, [])]
        
        while queue:
            curtStr, steps = queue.pop(0)
            if len(steps) >= len(target) * 10:
                continue
            if all(x == \"?\" for x in list(curtStr)):
                return steps[::-1]
            for i in range(len(curtStr) - len(stamp) + 1):
                if canStamp(curtStr, i, stamp):
                    queue.append((curtStr[:i] + \"?\" * len(stamp) + curtStr[i+len(stamp):], steps + [i]))
                    break
            
            
