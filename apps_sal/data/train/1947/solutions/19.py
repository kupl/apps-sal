import collections


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def aggregate_b(B):
            max_occurences = collections.defaultdict(list)
            for subset in B:
                letter_count = collections.Counter(subset)
                for (letter, count) in list(letter_count.items()):
                    if not max_occurences[letter] or count > max_occurences[letter]:
                        max_occurences[letter] = count
            return max_occurences
        result = []
        max_letter_occurences = aggregate_b(B)
        for word in A:
            letter_count = max_letter_occurences.copy()
            for letter in word:
                if letter in letter_count:
                    letter_count[letter] -= 1
                    if letter_count[letter] == 0:
                        del letter_count[letter]
            if not letter_count:
                result.append(word)
        return result
