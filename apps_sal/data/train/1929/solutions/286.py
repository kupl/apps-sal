# class StreamChecker:

#     def __init__(self, words: List[str]):
#         if len(words) ==0:
#             print(\"Empty list!\")
#         elif len(words) > 2000:
#             print(\"List is too long!\")
#         max_word_len,  min_word_len = max([len(word) for word in words]), min([len(word) for word in words])
#         if min_word_len == 0:
#             print(\"Word is empty string!\")
#         elif max_word_len > 2000:
#             print(\"Word is too long!\")
#         words_dict = {}
#         for word in words:
#             k = len(word)
#             words_dict[k] = words_dict.get(k,[]) + [word]
#         self.sorted_words = sorted(words_dict.items())
#         self.queries = ''
#         self.n_queries = 0

#     def query(self, letter: str) -> bool:
#         self.queries += letter
#         self.n_queries += 1
#         if self.n_queries > 40000:
#             print(\"The number of queries is more than 40000!\")
#         for k_words in self.sorted_words:
#             k, words = k_words[0], k_words[1]
#             s = self.queries[(self.n_queries - k):self.n_queries]
#             for word in words:
#                 if word == s:
#                     return True
#         return False
class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.dic[letter])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
