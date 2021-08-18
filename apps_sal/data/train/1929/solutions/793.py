class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False


class ReverseTrie:

    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            self.add_reverse_word(word)

    def add_reverse_word(self, word):
        curr_node = self.root

        for idx in range(len(word) - 1, -1, -1):
            char = word[idx]
            curr_node = curr_node.children[char]

        curr_node.end = True

    def reverse_word_exists(self, reverse_letters):
        reverse_word_found = False

        curr_trie_node = self.root
        for idx in range(len(reverse_letters) - 1, -1, -1):
            char = reverse_letters[idx]
            if char in curr_trie_node.children:
                curr_trie_node = curr_trie_node.children[char]
                if curr_trie_node.end:
                    return True

                idx -= 1
            else:
                return False

        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.last_n_queries = collections.deque([])
        self.trie_reverse_words = ReverseTrie(words)
        self.max_word_length = 2000

    def query(self, letter: str) -> bool:

        self.last_n_queries.append(letter)

        if len(self.last_n_queries) > self.max_word_length:
            self.last_n_queries.popleft()

        return self.trie_reverse_words.reverse_word_exists(self.last_n_queries)
