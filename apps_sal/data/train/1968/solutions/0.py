class Solution:
    def removeSubfolders(self, folder):
    
        folders = folder
    
        folders.sort()
        output = []
        parent = ' '
    
        for folder in folders:
            if not folder.startswith(parent):
                output.append(folder)
                parent = folder + '/'
    
        return output
