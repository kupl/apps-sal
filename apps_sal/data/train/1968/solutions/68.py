class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        # ans = [ folder[0]]
        # prev = folder[0] + '/'
        # for f in folder[1:]:
        #     if not f.startswith(prev):
        #         ans.append(f)
        #         prev = f+'/'
        # return ans
        
        #using set
        ans = []
        seen = set(folder)
        for i in folder:
            path = i
            while path:
                path = path[:path.rfind('/')]
                if path in seen:
                    break
            else:
                ans.append(i)
        return (ans)
