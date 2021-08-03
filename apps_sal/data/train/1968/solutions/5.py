class Trie:
    def __init__(self, *words):
        self._end = '_end'
        self.root = {}
        self.insert(*words)

    def insert(self, *words):
        _end = self._end
        root = self.root

        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
        return root

    def has(self, word):
        trie = self.root
        _end = self._end

        current_dict = trie
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return _end in current_dict


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if folder:
            folder.sort()

        r = []
        trie = Trie()
        for f in folder:
            names = [x for x in f.split('/') if x.strip()]
            to_insert = True
            for i in range(1, len(names) + 1):
                subfolder = '/'.join(names[:i])
                subfolder = '/' + subfolder if subfolder else subfolder
                if trie.has(subfolder):
                    to_insert = False
                    break

            if to_insert:
                r.append(f)
                trie.insert(f)
        return r
