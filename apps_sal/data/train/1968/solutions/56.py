# class Trie:
#     def __init__(self):
#         self.children = collections.defaultdict(Trie)
#         self.index = -1
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         self.root = Trie()

#         for i, f in enumerate(folder):
#             curr = self.root
#             for ch in f:
#                 curr = curr.children[ch]
#             curr.index = i
#         # print(self.root)
#         return self.bfs(self.root, folder)

#     def bfs(self, trie, folder):
#         q = [trie]
#         res = []

#         for node in q:
#             if node.index >= 0:
#                 res.append(folder[node.index])
#             else:
#                 for c in node.children:
#                     q.append(c)
#         return res
class Trie:
    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.index = -1


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()
        for i in range(len(folder)):
            curr = self.root
            for ch in folder[i]:
                curr = curr.sub[ch]
            curr.index = i
        return self.bfs(self.root, folder)

    def bfs(self, node, folder):
        q, ans = [node], []
        for t in q:
            if t.index >= 0:
                ans.append(folder[t.index])
            # else:
            for c in t.sub.keys():
                if c != '/' or t.index < 0:
                    q.append(t.sub.get(c))
        return ans
