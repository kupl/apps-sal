import re
from collections import defaultdict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        mapping = defaultdict(lambda: -1)
        ans = []
        for name in names:
            if name in mapping:
                count = mapping[name] + 1
                fname = f'{name}({count})'
                while fname in mapping: 
                    count += 1
                    fname = f'{name}({count})'
                mapping[name] = count
            else:
                fname = name
            mapping[fname] += 1
            ans.append(fname)
        return ans
