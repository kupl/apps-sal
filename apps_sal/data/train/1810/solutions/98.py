import re


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        original_names = set()
        modified_names = defaultdict(set)
        results = []
        
        for name in names:
            \"\"\"
            print(original_names)
            print(modified_names)
            \"\"\"
            
            if name not in original_names:
                original_names.add(name)
                
                if name[-1] == \")\":
                    i = len(name) - 2
                    while i > 0 and name[i - 1] != \"(\":
                        i -= 1
                    suffix = name[i:-1]
                    prefix = name[:i - 1]
                    modified_names[prefix].add(int(suffix))

                results.append(name)
            
            else:
                # modified_names[name] += 1
                x = 1
                while x in modified_names[name]:
                    x += 1
                modified_names[name].add(x)
                
                result = \"{}({})\".format(name, x)
                
                original_names.add(result)
                
                results.append(result)

        return results

