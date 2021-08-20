class StreamChecker:
    END = 0

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            ptr = self.trie
            for letter in word:
                if letter not in ptr:
                    ptr[letter] = {}
                ptr = ptr[letter]
            ptr[StreamChecker.END] = True
        self.working_list = []

    def query(self, letter: str) -> bool:
        is_word = False
        new_working_list = []
        self.working_list.append(self.trie)
        for working_ptr in self.working_list:
            if letter in working_ptr:
                new_working_ptr = working_ptr[letter]
                new_working_list.append(new_working_ptr)
                if StreamChecker.END in new_working_ptr:
                    is_word = True
        self.working_list = new_working_list
        return is_word
