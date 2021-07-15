def vowel_indices(word):
    word = word.lower()
    vowels = ['a','e','i','o','u','y']
    return [i+1 for i in range(len(word)) if word[i] in vowels ]

