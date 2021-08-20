class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        exists = set()
        last = collections.defaultdict(int)
        result = []
        for name in names:
            k = last[name]
            modified = name
            while modified in exists:
                k += 1
                modified = f'{name}({k})'
            last[name] = k
            result.append(modified)
            exists.add(modified)
        return result
