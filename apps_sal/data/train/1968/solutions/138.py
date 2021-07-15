class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort(key = lambda x: len(x))
        res = []
        # while folder:
        #     e = folder.pop()
        #     for p in folder:
        #         if e.startswith(p) and e[len(p)] == '/':
        #                 e = ''   
        #                 break
        #     if e: res.append(e)
        # return res
    
        # trie = {}
        # for t in folder:
        #     m = trie
        #     parent = False
        #     for c in t.split('/'):
        #         m[c] = m.get(c, {})
        #         m = m[c]
        #         if '$' in m: 
        #             parent = True
        #             break
        #     if not parent:
        #         m[\"$\"] = '$'
        #         res.append(t)
        # return res
         
#             use stack and sort with lexinton
        files = sorted(folder)
        stack  = [files[0]]
        for i in range(1, len(files)):
            if not files[i].startswith(stack[-1] + '/'):  stack.append(files[i])
        return stack

