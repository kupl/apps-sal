from pprint import pprint as pp
class Solution:
    def removeSubfolders2(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        st = set()
        for f in folder:
            for i in range(len(f)):
                if f[i] == \"/\" and i > 0:
                    if f[:i] in st:
                        break
            else:
                st.add(f)
        return list(st)
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        def insert(t, word):
            for w in word:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t['#'] = word
        for f in folder:
            word = f.split('/')[1:]
            insert(trie, word)
        def dfs(t):
            if '#' in t:
                return ['/' + '/'.join(t['#'])]
            res = []
            for w in t:
                res += dfs(t[w])
            return res
        return dfs(trie)
