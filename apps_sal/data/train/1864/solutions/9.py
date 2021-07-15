class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        res = set()
        queue = []
        queue.append(expression)
        seen = set()
        while queue:
            n = len(queue)
            
            for i in range(n):
                exp = queue.pop(0)
                
                if exp in seen:
                    continue
                else:
                    seen.add(exp)
                
                if exp.find(\"{\") == -1:
                    res.add(exp)
                    continue
                    
                for j in range(len(exp)):
                    if exp[j] == \"}\":
                        right = j
                        break
                    
                    if exp[j] == \"{\":
                        left = j
                
                arr = exp[left+1:right].split(\",\")
                
                for element in arr:
                    queue.append(exp[:left] + element + exp[right+1:])
                
        return sorted(list(res))
        
