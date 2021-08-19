class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        from collections import defaultdict
        seen = set()
        hashmap = defaultdict(int)
        ans = []
        for name in names:
            # if name not in hashmap, k == 0
            k = hashmap[name]
            current = name
            while current in seen:
                k += 1
                current = f'{name}({k})'
            hashmap[name] = k
            seen.add(current)
            ans.append(current)
        return ans
