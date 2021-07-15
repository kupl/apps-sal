class Solution:
    def init(self, folder):
        self.tries = {}
        for f_ in folder:
            f_list = list(filter(None, (f_.strip()+'/$').split(\"/\")))
            node = self.tries
            for folder in f_list:
                if folder not in node:
                    node[folder] = {}
                node = node[folder]

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        if folder == None or len(folder) == 0:
            return result
        
        self.init(folder)
        for f_ in folder:
            path = []
            node = self.tries
            f_list = list(filter(None, f_.strip().split(\"/\")))
            for folder in f_list:
                if '$' in node:
                    break
                path.append(folder)
                node = node[folder]

            if \"/\"+\"/\".join(path) not in result:
                result.append(\"/\"+\"/\".join(path))
            
        return result
                



        
        
