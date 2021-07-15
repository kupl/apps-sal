class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Questions:are all char in the order? any missing? any duplicates?
        
        O(wn) len of longest word, compare all words
        order would be in a map to see
        
        '''
        word_indexes = {ch : i for i, ch in enumerate(list(order))}
        
        for i, word1 in enumerate(words[1:], start=1):
            word2 = words[i-1] # word before
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]: # only compare when they are different
                    if word_indexes[word1[j]] < word_indexes[word2[j]]:
                        return False
                    break
            else: # when break not hit
                # complete word but there is more characters for one of the words: 
                # should be ordered after the shorter word
                if len(word1) < len(word2):
                    # word before is longer
                    return False
        
        return True
