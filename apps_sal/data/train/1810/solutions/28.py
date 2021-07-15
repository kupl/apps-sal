class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        folders = {}
        for n in names:
            if n not in folders:
                folders[n] = 1
                ans.append(n)
            else:
                i = folders[n]
                while f'{n}({i})' in folders:
                    i += 1
                ans.append(f'{n}({i})')
                folders[f'{n}({i})'] = 1
                folders[n] = i+1
        return ans
