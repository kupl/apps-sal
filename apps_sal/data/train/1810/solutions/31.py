class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        next_valid_names = {}
        ans = []
        
        for name in names:
            if name not in next_valid_names:
                ans.append(name)
                next_valid_names[name] = 1
            else:
                index = next_valid_names[name]
                while f\"{name}({index})\" in next_valid_names:
                    index += 1
                ans.append(f\"{name}({index})\")
                next_valid_names[f\"{name}({index})\"] = 1
                next_valid_names[name] = index+1
        return ans
