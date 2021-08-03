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
        searches = self.searches
        searches.append(self.root)

        found = False
        updated_searches = []
        for search in searches:
            if letter not in search:
                continue
            search = search[letter]
            updated_searches.append(search)
            if '$' in search:
                found = True
        self.searches = updated_searches

        return found
