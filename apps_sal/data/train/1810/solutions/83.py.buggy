class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        result = []
        name_counts = {}  # Name :-> count
        result_set = set()
        
        for name in names:
            if name not in name_counts:
                name_counts[name] = 1
            
            prev_count = name_counts[name]
            
            new_name = name
            while new_name in result_set:
                name_counts[name] += 1
                new_name = f\"{name}({prev_count})\"
                prev_count += 1
            
            
            result.append(new_name)
            result_set.add(new_name)
        
        return result
