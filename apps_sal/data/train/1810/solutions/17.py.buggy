class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        uniq = set()
        ans = []
        for name in names:
            if name in uniq:
                k = 1
                while(f\"{name}({k})\" in uniq):
                    k+=1
                uniq.add(f\"{name}({k})\")
                ans.append(f\"{name}({k})\")
            else:
                uniq.add(name)
                ans.append(name)
        return ans
