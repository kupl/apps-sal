class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        existing = {}
        output = []
        for name in names:
            if name not in existing.keys():
                existing[name] = 1
                output.append(name)
            else:
                # find a name
                k = existing[name]
                while True:
                    new_name = '{}({})'.format(name, k)
                    if new_name not in existing:
                        existing[new_name] = 1
                        existing[name] = k+1
                        output.append(new_name)
                        break
                    k += 1
        return output
