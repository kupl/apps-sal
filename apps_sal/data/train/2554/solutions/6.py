class Solution:

    def longestWord(self, words):
        words.sort()
        longest_word = ''
        word_list = list()
        words_set = set([''])
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(longest_word) < len(word):
                    longest_word = word
        return longest_word
