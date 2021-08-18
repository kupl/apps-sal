def vowel_indices(word):
    count = []
    words = word.lower()

    for i in range(len(words)):
        if words[i] in "aeiouy":
            count.append(i + 1)

    return count
