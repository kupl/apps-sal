class Solution:

    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        output = []
        parent = ' '
        for folder in folders:
            if not folder.startswith(parent):
                output.append(folder)
                parent = folder + '/'
        return output
