class Node:

    def __init__(self, v):
        self.v = v
        self.children = {}

    def __repr__(self):
        return f'Node({self.v} {self.children.keys()})'


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Node('')
        for f in folder:
            self.add_to_trie(trie, f)
        return ['/' + '/'.join(i) for i in self.dfs(trie)]

    def dfs(self, cur):
        if not cur.children:
            return [[]]
        res = []
        for (child, child_node) in cur.children.items():
            for sub_res in self.dfs(child_node):
                res.append([child] + sub_res)
        return res

    def add_to_trie(self, trie, f):
        if not f:
            return
        sub_folders = f.split('/')[1:]
        if sub_folders[0] in trie.children:
            cur = trie
            for (i, sub_folder) in enumerate(sub_folders):
                if sub_folder not in cur.children and (not cur.children):
                    return
                elif sub_folder not in cur.children:
                    self.add_subs_to_trie(cur, i, sub_folders)
                    return
                else:
                    cur = cur.children[sub_folder]
            if cur.children:
                cur.children = {}
        else:
            self.add_subs_to_trie(trie, 0, sub_folders)

    def add_subs_to_trie(self, trie, ix, sub_folders):
        cur = trie
        for i in range(ix, len(sub_folders)):
            sub_folder = sub_folders[i]
            cur.children[sub_folder] = Node(sub_folder)
            cur = cur.children[sub_folder]
