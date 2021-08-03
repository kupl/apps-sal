class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = defaultdict(int)
        ans = []
        for name in names:
            if name not in used:
                ans.append(name)
                used[name] += 1
            else:
                num = used[name]
                tmp = f'{name}({used[name]})'
                while tmp in used:
                    num += 1
                    tmp = f'{name}({num})'
                ans.append(tmp)
                if tmp not in used:
                    used[tmp] = 1
                used[name] = max(used[name] + 1, num)
        return ans
