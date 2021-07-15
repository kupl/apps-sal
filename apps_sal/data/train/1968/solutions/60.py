class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.child = {}
                self.is_word = False
            def add(self,word):
                curr = self
                for w in word:
                    if w not in curr.child:
                        curr.child[w] = Trie()
                    curr = curr.child[w]
                curr.is_word = True
            def get_val(self,word):
                curr = self
                ans = \"\"
                for w in word:
                    if w in curr.child:
                        ans += w
                        curr = curr.child[w]
                        if curr.is_word and \"/\" in curr.child:
                            return ans
                return ans
        def remove_dir(folders):
            trie = Trie()
            ans = set()
            for f in folders:
                trie.add(f)
            for f in folders:
                ans.add(trie.get_val(f))
            return list(ans)
        return remove_dir(folder)
