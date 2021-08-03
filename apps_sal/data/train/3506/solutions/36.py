vowel = "aeiouy"


def vowel_indices(word):
    ans = []
    for i in range(len(word)):
        if word[i].lower() in vowel:
            ans.append(i + 1)
    return ans
