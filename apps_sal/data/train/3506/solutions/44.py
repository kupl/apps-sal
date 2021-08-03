def vowel_indices(word):
    pw = []
    vowles = "aeiouy"
    for i in range(len(word)):
        if word[i].lower() in vowles:
            pw.append(i + 1)
    return pw
