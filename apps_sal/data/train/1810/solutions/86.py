class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # from collections import defaultdict
        # hashmap = defaultdict(int)
        hashmap = {}

        seen = set()
        ans = []
        for name in names:
            # k = hashmap[name] # if defaultdict(int) is used
            k = hashmap.setdefault(name, 0)  # if ordinary dict is used
            current = name
            while current in seen:
                k += 1
                current = f'{name}({k})'
            hashmap[name] = k
            seen.add(current)
            ans.append(current)
        return ans
