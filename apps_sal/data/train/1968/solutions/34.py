class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s = set()
        folder.sort(key=len)
        for i in folder:
            f = 0
            x = i.split('/')
            temp = \"\"
            for j in x:
                if j==\"\":
                    continue
                temp = temp + '/'+j
                if temp in s:
                    f = 1
                    break
            if f==0:
                s.add(i)
        return list(s)
