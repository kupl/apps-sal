class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        seen = set()
        for path in folder:
            if not any(path[i] == '/' and path[:i] in seen for i in range(2, len(path))):
                seen.add(path)
        return seen


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
