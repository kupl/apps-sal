class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x:len(x))
        folderDict = {}
        ans = set(folder)
        
        # ans = []
        for address in folder:
            aList = (address[1:]).split('/')
            # print(address, aList)
            pointer = folderDict
            for name in aList:
                if name in pointer:
                    pointer = pointer[name]
                    if '$' in pointer:
                        if address in ans:
                            # print('remove', address)
                            ans.remove(address)
                else:
                    pointer[name] = {}
                    pointer = pointer[name]
            pointer['$'] = ''
        # print(folderDict)
        return ans
