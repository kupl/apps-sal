class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # Since a universal word needs to be superset for all words in B, we can combine all words in B
        #   to become a new word, and words in A only need to have this one single word as its subset

        # get a list of ints of length 26 to represent how many of each letter is in a word
        def countLetter(s):
            res = [0] * 26
            for c in s:
                res[ord(c) - ord('a')] += 1
            return res

        # get how many of each letter is in the combined letter of B, note that we only need the larger
        #   number if one char appears in two different words. Ex: 'lo' and 'loo' will become 'loo'
        b_count = [0] * 26
        for b in B:
            for i, c in enumerate(countLetter(b)):
                b_count[i] = max(b_count[i], c)

        # get all words x with count(x) greater than b_count in every character
        return [x for x in A if all([a_count >= b_count for a_count, b_count in zip(countLetter(x), b_count)])]
