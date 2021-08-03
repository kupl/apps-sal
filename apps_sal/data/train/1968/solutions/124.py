class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        tokens = {path: path.split('/') for path in folder}
        for path in folder:
            curr = trie
            for token in tokens[path]:
                if token not in curr:
                    curr[token] = {}
                curr = curr[token]
            curr['#'] = True

        paths = set(folder)
        for path in folder:
            curr = trie
            for token in tokens[path]:
                if '#' in curr:
                    paths.remove(path)
                    break
                curr = curr[token]
        return list(paths)
