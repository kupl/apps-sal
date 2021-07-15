class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        _map, ans = defaultdict(int), []
        
        for name in names:
            if _map[name] > 0:
                print(name)
                while name + '(' + str(_map[name]) + ')' in _map:
                    _map[name] += 1
                ans.append(name + '(' + str(_map[name]) + ')')
                _map[name + '(' + str(_map[name]) + ')'] += 1
                _map[name] += 1
            else:
                _map[name] += 1
                ans.append(name)
            
        
        return ans
