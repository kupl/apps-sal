class Trie:
    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.index = -1


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()
        for i in range(len(folder)):
            cur = self.root
            for c in folder[i]:
                cur = cur.sub[c]
            cur.index = i
        return self.bfs(self.root, folder)

    def bfs(self, trie: Trie, folder: List[str]) -> List[str]:
        q, ans = [trie], []
        for t in q:
            if t.index >= 0:
                ans.append(folder[t.index])
            for c in list(t.sub.keys()):
                if '/' != c or t.index < 0:
                    q.append(t.sub.get(c))
        return ans
        # folder.sort()
        # ans = []
        # for f in folder:
        #     if not ans or not f.startswith(ans[-1] + '/'):
        #         ans.append(f)
        # return ans

        # folder.sort()
        # seen = set()
        # for path in folder:
        #     if not any(path[i] == '/' and path[:i] in seen for i in range(2, len(path))):
        #         seen.add(path)
        # return seen


# Trie
#         trie = {}
#         for path in folder:
#             curr = trie
#             for f in path.split('/'):
#                 if f in curr:
#                     curr = curr[f]
#                 else:
#                     curr[f] = {}
#                     curr = curr[f]
#             curr[None] = None

#         res = []
#         for path in folder:
#             curr = trie
#             issub = False
#             for f in path.split('/'):
#                 if None in curr:
#                     issub = True
#                 else:
#                     curr = curr[f]
#             if not issub:
#                 res.append(path)

#         return res
