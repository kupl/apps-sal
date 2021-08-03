def palindrome_pairs(words):
    indices = []

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                concatenation = str(words[i]) + str(words[j])
                if concatenation == concatenation[::-1]:
                    indices.append([i, j])

    return indices
