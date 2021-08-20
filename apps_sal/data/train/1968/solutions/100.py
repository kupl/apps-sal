class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for path in folder:
            tokens = path.split('/')
            curr = trie
            for token in tokens:
                if token not in curr:
                    curr[token] = {}
                curr = curr[token]
            curr['#'] = True
        paths = set(folder)
        for path in folder:
            tokens = path.split('/')
            curr = trie
            for token in tokens:
                if '#' in curr:
                    paths.remove(path)
                    break
                curr = curr[token]
        return list(paths)
