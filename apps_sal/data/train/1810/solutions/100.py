class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used_names = set()
        suffixes = defaultdict(set)
        results = []
        
        for name in names:
            if name not in used_names:
                used_names.add(name)
                
                if name[-1] == \")\":
                    i = len(name) - 2
                    while i > 0 and name[i - 1] != \"(\":
                        i -= 1
                    suffix = name[i:-1]
                    prefix = name[:i - 1]
                    suffixes[prefix].add(int(suffix))
            
            else:
                x = 1
                while x in suffixes[name]:
                    x += 1
                suffixes[name].add(x)
                
                name = \"{}({})\".format(name, x)
                
                used_names.add(name)
            
            results.append(name)

        return results

