class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        s = set()
        ans = []
        
        for name in names:
            if name not in s:
                s.add(name)
                ans.append(name)
            else:
                for i in range(1, 2 ** 20):
                    if f\"{name}({i})\" not in s:
                        s.add(f\"{name}({i})\")
                        ans.append(f\"{name}({i})\")
                        break
        return ans
