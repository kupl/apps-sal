class Solution:
            
    def getFolderNames1(self, names: List[str]) -> List[str]:
        memo = dict()
        seen = set()
        sol = []
        for s in names:
            # print (s, sol)
            
            if s and s[-1]==')':
                if s in memo:
                    memo[s] += 1
                else:
                    memo[s] = 0
                base = s
            else:
                base = s
                memo[base] = 0
                
                
            k = memo[base]
            while True:
                if k==0:
                    target = base
                else:
                    target = base+'('+str(k)+')'
                if target in seen:
                    k += 1
                else:
                    sol.append(target)
                    seen.add(target)
                    break
            memo[base] = k
        return sol
    

    
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = set()
        sol = []
        for s in names:
            if s in seen:
                k = 1
                target = f'{s}({k})'
                while target in seen:
                    k += 1
                    target = f'{s}({k})'
                sol.append(target)
                seen.add(target)
            else:
                sol.append(s)
                seen.add(s)
                
        return sol
    
#     def getFolderNames(self, names: List[str]) -> List[str]:
# \t\t# Edge case: names is empty.
#         if not names:
#             return []
        
#         assignedNames = set()
#         uniqueNames = []
        
#         for name in names:
#             if name in assignedNames:
#                 k = 1
#                 numberedName = f'{name}({k})'
                
#                 while numberedName in assignedNames:
#                     k += 1
#                     numberedName = f'{name}({k})'
                
#                 assignedNames.add(numberedName)
#                 uniqueNames.append(numberedName)
#             else:
#                 assignedNames.add(name)
#                 uniqueNames.append(name)
            
#         return uniqueNames

