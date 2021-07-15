from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = dict()

        for word in words:
            root = self.root
            for c in word:
                if c not in root:
                    root[c] = dict()
                root = root[c]
            root['$'] = '.'
        
        self.searches = []
        

    def query(self, letter: str) -> bool:
        self.searches.append(self.root)

        found = False
        failed = list()
        i = 0
        for search in self.searches:
            if letter not in search:
                failed.append(i)
            else:
                search = search[letter]
                self.searches[i] = search
                if '$' in search:
                    found = True
            i += 1
        
        o = 0
        for i in failed:
            del self.searches[i - o]
            o += 1
        
        return found


