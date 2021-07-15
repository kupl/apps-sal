class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_counts = {}
        for word in B:
            word_counts = {}
            for letter in word:
                if letter in word_counts:
                    word_counts[letter] += 1
                else:
                    word_counts[letter] = 1
            for letter in word_counts:
                if letter in b_counts:
                    b_counts[letter] = max(b_counts[letter], word_counts[letter])
                else:
                    b_counts[letter] = word_counts[letter]
        result = []
        for word in A:
            a_counts = {}
            for letter in word:
                if letter in a_counts:
                    a_counts[letter] += 1
                else:
                    a_counts[letter] = 1
            superset = True
            for key in b_counts:
                if key not in a_counts or b_counts[key] > a_counts[key]:
                    superset = False
                    break
            if superset:
                result.append(word)
        return result
