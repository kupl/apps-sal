def vowel_indices(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    letters = list(word)
    answer = list()
    i = 0
    while i < len(letters):
        if letters[i] in vowels:
            answer.append(i + 1)
        i = i + 1
    return answer
