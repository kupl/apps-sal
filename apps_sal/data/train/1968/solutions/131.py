class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        splitted = list(map(lambda path: path.split('/')[1:], folder))
        numPath = len(folder)
        i = 0
        while i < numPath:
            result.append(folder[i])
            current = splitted[i]
            while i < numPath:
                remove = True
                for k in range(min(len(splitted[i]), len(current))):
                    if splitted[i][k] != current[k]:
                        remove = False
                        break
                if remove:
                    i += 1
                else:
                    break
        return result
