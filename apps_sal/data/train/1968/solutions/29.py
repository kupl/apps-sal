class Node:

    def __init__(self):
        self.next = {}
        self.folder = False


class Trie:

    def __init__(self):
        self.root = Node()

    def update(self, folder):
        start = 1
        node = self.root
        while node and start < len(folder):
            i = start
            while i < len(folder) and folder[i] != '/':
                i += 1
            curr_fold = folder[start:i]
            if curr_fold not in node.__next__:
                node.next[curr_fold] = Node()
            node = node.next[curr_fold]
            start = i + 1
        node.folder = True

    def find_all(self):
        output = []

        def helper(node, path):
            if node.folder:
                output.append(path)
            else:
                for next_node in node.__next__:
                    helper(node.next[next_node], path + '/' + next_node)
        helper(self.root, '')
        return output


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_trie = Trie()
        for fold in folder:
            folder_trie.update(fold)
        return folder_trie.find_all()
