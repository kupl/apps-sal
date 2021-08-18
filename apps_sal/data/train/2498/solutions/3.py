class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        if len(words) == 1:
            return True

        i = 0

        lex_dict = {l: o for o, l in enumerate(order)}
        print(lex_dict)

        prev_word = words[0]
        for i in range(1, len(words)):
            word = words[i]
            for l1, l2 in zip(prev_word, word):
                if lex_dict[l2] < lex_dict[l1]:
                    return False
                elif lex_dict[l2] > lex_dict[l1]:
                    break
            else:
                if len(prev_word) > len(word):
                    return False
            prev_word = word

        return True
