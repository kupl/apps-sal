class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        if len(folder) == 1:
            return folder
        
        #def is_subfolder(folder1, folder2):
        #    s_f1 = folder1.split('/')
        #    s_f2 = folder2.split('/')
        #    
        #    if len(s_f1) < len(s_f2):
        #        i = 0
        #        while i < len(s_f1):
        #            if s_f1[i] == s_f2[i]:
        #                i += 1
        #            else:
        #                return False
        #        return True
                    
        
        
        folder.sort()
        #for i,j in enumerate(folder):
        i = 0
        while i < len(folder) - 1:
                #
                #if is_subfolder(folder[i], folder[i+1]):
                #if len(folder[i+1]) > len(folder[i]):
            #if folder[i+1].startswith('{}/'.format(folder[i])):
            if folder[i+1].startswith(folder[i]+'/'):
            #if '{}/'.format(folder[i]) == folder[i+1][:(len(folder[i])+1)]:
                folder.pop(i+1)
            else:
                i+=1
            
        return folder    

