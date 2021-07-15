class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        used_names = set()
        counter = dict()
        
        result = []
        
        for name in names:
            
            value = counter.get(name, 0)
            current = name
            
            while current in used_names:
                value += 1  # update the value
                current = f\"{name}({value})\"  # update the current
            
            counter[name] = value
            # print(f\"Counter: {counter}\")
            used_names.add(current)
            result.append(current)
        
        return result
