class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        hashmap = {}
        seen = set()
        ans = []
        for name in names:
            k = hashmap.setdefault(name, 0)
            current = name
            while current in seen:
                k += 1
                current = f'{name}({k})'
            hashmap[name] = k
            seen.add(current)
            ans.append(current)
        return ans
