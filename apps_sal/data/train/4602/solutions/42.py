# write the function is_anagram
def is_anagram(test, original):
    test_word_freq = {}
    original_word_freq = {}

    test = test.lower()
    original = original.lower()

    if len(test) == len(original):
        for idx, letter in enumerate(test):
            if letter not in test_word_freq:
                test_word_freq[letter] = 1
            else:
                test_word_freq[letter] += 1

        for idx, lett in enumerate(original):
            if lett not in original_word_freq:
                original_word_freq[lett] = 1
            else:
                original_word_freq[lett] += 1
        print(original_word_freq)
        print(test_word_freq)
        for k, v in list(test_word_freq.items()):
            if k not in original_word_freq:
                return False
            if v != original_word_freq[k]:
                return False
        return True
    else:
        return False
