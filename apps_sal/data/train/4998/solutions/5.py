from collections import Counter


def wanted_words(n, m, forbid_let):
    result = []

    for word in WORD_LIST:                                        # for each word in word list
        if len(word) == n + m:                                    # if word length is correct
            letters = Counter(word)                               # create a count of letters

            if (sum(letters[c] for c in "aeiou") == n            # if vowel count is correct
                    and all(c not in word for c in forbid_let) ):     # and has no forbidden letters
                result.append(word)                               # add to the results

    return result
