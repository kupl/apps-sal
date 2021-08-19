# Time & space: O(n * m), where n = folder.length, m = average size of the strings in folder.
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.path = None


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for directory in folder:
            curr = self.root
            for f in directory.split('/')[1:]:
                if f not in curr.children:
                    curr.children[f] = TrieNode()
                curr = curr.children[f]
            curr.path = directory

        def trie_search(node, res):  # dfs
            if node.path:
                res.append(node.path)
                return res
            for nbr in node.children:
                res = trie_search(node.children[nbr], res)
            return res

        return trie_search(self.root, [])

# # Sort the folders;
# # For each folder check if the followings are child folders; if yes, ignore; otherwise, count it in.
# # Time: O(n * m * log(n)), space: O(1)(excluding space cost of sorting part), where n = folder.length, m = average size of the strings in folder.
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#             ans = []
#             for f in sorted(folder):
#                 if not ans or not f.startswith(ans[-1] + '/'):\t#  need '/' to ensure a parent.
#                     ans.append(f)
#             return ans
