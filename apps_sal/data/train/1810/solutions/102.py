class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used_names = set()
        # suffixes = defaultdict(set)
        suffixes = {}
        results = []
        
        for name in names:
            # print(suffixes)
            
            if name not in used_names:
                used_names.add(name)
                
                if name[-1] == \")\":
                    i = len(name) - 2
                    while i > 0 and name[i - 1] != \"(\":
                        i -= 1
                    suffix = int(name[i:-1])
                    prefix = name[:i - 1]
                    # suffixes[prefix].add(suffix)
                    if prefix not in suffixes:
                        suffixes[prefix] = [{suffix}, 1]
                    else:
                        suffixes[prefix][0].add(suffix)
            
            else:
                \"\"\"
                x = 1
                while x in suffixes[name]:
                    x += 1
                suffixes[name].add(x)
                \"\"\"
                if name not in suffixes:
                    x = 1
                    suffixes[name] = [{1}, 1]
                else:
                    x = 1
                    while x in suffixes[name][0]:
                        x += 1
                    suffixes[name][0].add(x)
                    suffixes[name][1] = x
                
                name = \"{}({})\".format(name, x)
                used_names.add(name)
            
            results.append(name)

        return results

