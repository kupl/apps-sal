class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s_f = sorted(folder)
        root = {}
        result = []
        for i in range(len(s_f)):
            path = s_f[i]
            p_arr = path.split(\"/\")[1:]
            cur = root
            for j in range(len(p_arr)):
                if -1 in cur:
                    break
                #abc
                if p_arr[j] not in cur:
                    cur[p_arr[j]] = {}
                cur = cur[p_arr[j]]
                if j == len(p_arr) - 1:
                    cur[-1] = i
                    result.append(path)
        return result
            
            
