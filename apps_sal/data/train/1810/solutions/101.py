class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        original_names = set()
        suffixes = defaultdict(set)
        results = []
        
        for name in names:
            if name not in original_names:
                original_names.add(name)
                
                if name[-1] == \")\":
                    i = len(name) - 2
                    while i > 0 and name[i - 1] != \"(\":
                        i -= 1
                    suffix = name[i:-1]
                    prefix = name[:i - 1]
                    suffixes[prefix].add(int(suffix))

                results.append(name)
            
            else:
                x = 1
                while x in suffixes[name]:
                    x += 1
                suffixes[name].add(x)
                
                result = \"{}({})\".format(name, x)
                
                original_names.add(result)
                
                results.append(result)

        return results

