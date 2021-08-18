class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Questions:are all char in the order? any missing? any duplicates?

        O(wn) len of longest word, compare all words
        order would be in a map to see

        '''
        word_indexes = {ch: i for i, ch in enumerate(list(order))}

        for i, word1 in enumerate(words[1:], start=1):
            word2 = words[i - 1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word_indexes[word1[j]] < word_indexes[word2[j]]:
                        return False
                    break
            else:
                if len(word1) < len(word2):
                    return False

        return True
