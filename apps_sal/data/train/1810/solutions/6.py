class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        hashmap = {}
        res = []
        
        for name in names:
            if name not in hashmap:
                hashmap[name] = True
                res.append(name)
            else:
                i = 1
                _name = f'{name}({i})'
                while _name in hashmap:
                    i += 1
                    _name = f'{name}({i})'
                hashmap[_name] = True
                res.append(_name)
        return res
