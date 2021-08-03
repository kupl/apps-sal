class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # shorter strings with common alphabets are always preferred in ordering
        # given the order, a O(m) dictionary mapping letter to a number can be made
        # and by iterating through every word and computing the sum of numbers,
        # when the number is smaller for earlier one, then terminate with False
        # if the loop finishes without returning False, then return True

        if len(words) == 1:
            return True

        i = 0

        lex_dict = {l: o for o, l in enumerate(order)}
        print(lex_dict)
        # for o in range(len(order)):
        #     lex_dict[order[o]] = o + 1

        # instead of scrolling through each letter in all words,
        # just compare the pairs in the order (list is an ordered data structure anyway)

        prev_word = words[0]
        for i in range(1, len(words)):
            word = words[i]
            # do comparison
            # print(\"prev_word: {}, word: {}\".format(prev_word, word))
            for l1, l2 in zip(prev_word, word):
                if lex_dict[l2] < lex_dict[l1]:
                    return False
                elif lex_dict[l2] > lex_dict[l1]:
                    break  # no need for further checking
            # # handle special case, if it survived and the length of prev_word is > word, return False
            else:  # amazing trick! if no breakpoint occurred in the above for-loop, then come here
                if len(prev_word) > len(word):
                    return False
            prev_word = word

        return True
