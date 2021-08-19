# trie (dictionary tree)
# time complexity: O(NM), N = len(folder), M = len(folder[0])
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 1st step
        # build the dictionary tree
        trie = dict()
        trie[''] = [0, dict()]
        for f in folder:
            curr = trie
            prev = None
            for c in f.split('/'):
                if c not in curr:
                    curr[c] = [0, dict()]
                # print(f'c=|{c}|')
                prev = curr
                curr = curr[c][1]
            prev[c][0] = 1

        # 2nd step
        # traverse the dictionary tree in pre order, find the highest node with 1 of each subtree
        clean = []
        stack = [([''], trie[''])]  # path, node
        while stack:
            p, (isPath, d) = stack.pop()
            if isPath == 0:
                for c in d:
                    stack.append((p + [c], d[c]))
            else:
                clean.append('/'.join(p))
        return clean
