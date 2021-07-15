class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 1. iterate through the folders in the list
        # 2. split the folder by '/'
        # 3. check if names[:-1] exists in a dict
        # 4. if it exists, skip (drop) the folder
        # 5. if not, add names[:-1] to the dict and add the folder to the output list
        
        d = {}
        for f in folder:
            names = ''.join(f.split('/'))
            if len(names) > 0:
                d[names] = f
        
        output = []
        for f in folder:
            names = ''.join(f.split('/')[:-1])
            if not [True for i in range(len(names)) if names[:i+1] in d]:
                output.append(f)
                
        return output

