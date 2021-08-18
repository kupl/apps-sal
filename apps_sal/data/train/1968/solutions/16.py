class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        folderDict = {}
        ans = set(folder)

        for address in folder:
            aList = (address[1:]).split('/')
            pointer = folderDict
            for name in aList:
                if name in pointer:
                    pointer = pointer[name]
                    if '$' in pointer:
                        if address in ans:
                            ans.remove(address)
                else:
                    pointer[name] = {}
                    pointer = pointer[name]
            pointer['$'] = ''
        return ans
