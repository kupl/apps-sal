class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        # print(folder)
        l = len(folder)
        i = 0
        while(i < l - 1):
            p = folder[i]
            j = i + 1
            l = len(folder)
            while(j < l):
                if folder[j].startswith(p):
                    if len(folder[j]) > len(p) and folder[j][len(p)] == '/':
                        folder.remove(folder[j])
                        l = len(folder)
                    else:
                        j += 1
                else:
                    break

            i += 1
        return folder
