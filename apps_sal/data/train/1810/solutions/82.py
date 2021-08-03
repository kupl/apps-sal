class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        from collections import defaultdict
        seen = set()
        # hashmap = defaultdict(int)
        hashmap = {}
        ans = []
        for name in names:
            # if name not in hashmap, defaultdict will assgin 0 to k
            # k = hashmap[name]
            k = hashmap.setdefault(name, 0)
            current = name
            while current in seen:
                k += 1
                current = f'{name}({k})'
            hashmap[name] = k
            seen.add(current)
            ans.append(current)
        return ans
