class Trie:
    _end = '_end_'

    def __init__(self, words):
        self.root = dict()
        self.where = [self.root]
        self.delete = set()
        for word in words:
            current_dict = self.root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[Trie._end] = Trie._end

    def next(self, letter):
        ret = False
        self.where.append(self.root)
        for (i, where) in enumerate(self.where):
            if letter not in where:
                self.delete.add(i)
            else:
                self.where[i] = where[letter]
                if Trie._end in where[letter]:
                    ret = True
        for i in reversed(sorted(self.delete)):
            del self.where[i]
        self.delete = set()
        return ret

    def to_delete(self):
        return self.delete

    def has(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return Trie._end in current_dict

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[Trie._end] = Trie._end


class StreamChecker:

    def __init__(self, words):
        self.Trie = Trie(words)

    def query(self, letter):
        return(self.Trie.next(letter))
