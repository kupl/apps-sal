def is_anagram(test, original):
    def to_dict(word):
        dictionary = {}

        for w in word.lower():
            if w not in dictionary:
                dictionary[w] = 0
            else:
                dictionary[w] += 1

        return dictionary

    return to_dict(test) == to_dict(original)
