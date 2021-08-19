# class Solution:
#    def removeSubfolders(self, folder: List[str]) -> List[str]:
#         # Brute Force => TLE
#         # Time: O(n^2)
#         # Space: O(1)
#         def isSublist(shorter_path: List[str], longer_path: List[str]) -> bool:
#             if len(shorter_path) > len(longer_path):
#                 return False
#             for i in range(len(shorter_path)):
#                 if shorter_path[i] != longer_path[i]:
#                     return False
#             return True
#         res = []
#         n = len(folder)
#         for i in range(n):
#             is_subfolder = False
#             longer_path = folder[i].split('/')
#             for j in range(n):
#                 if j != i:
#                     shorter_path = folder[j].split('/')
#                     if isSublist(shorter_path, longer_path):
#                         is_subfolder = True
#                         break
#             if not is_subfolder:
#                 res.append(folder[i])
#         return res
#         # Sort alphabetically + Stack
#         # Time: O(nlogn)
#         # Space: O(1)
#         folder.sort()
#         stack = [folder[0]]
#         n = len(folder)
#         i = 1
#         while i < n:
#             shorter_path = stack[-1].split('/')
#             longer_path = folder[i].split('/')
#             if not isSublist(shorter_path, longer_path):
#                 stack.append(folder[i])
#             i += 1
#         return stack

# Trie
# Time: O(n)
# Space: O(n)
class Node:
    def __init__(self):
        self.children = {}
        self.isLeaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, path: List[str]) -> None:
        node = self.root
        for directory in path:
            if directory not in node.children:
                node.children[directory] = Node()
            node = node.children[directory]
        node.isLeaf = True

    def search(self, path: List[str]) -> bool:
        node = self.root
        for directory in path:
            if directory not in node.children:
                return False
            node = node.children[directory]
        return node.isLeaf

    def startWith(self, path: List[str]) -> bool:
        node = self.root
        for directory in path:
            if directory not in node.children:
                return False
            node = node.children[directory]
        return True

    def isSubfolder(self, path: List[str]) -> bool:
        node = self.root
        for directory in path:
            if node.isLeaf:
                return True
            node = node.children[directory]
        return False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            directories = path.split('/')
            trie.insert(directories)

        res = []
        for path in folder:
            directories = path.split('/')
            if not trie.isSubfolder(directories):
                res.append(path)
        return res
