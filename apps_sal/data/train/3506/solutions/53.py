def vowel_indices(word):
    vowels = 'aeiouy'
    list = []
    counter = 0
    word = word.lower()
    for letter in word:
        counter += 1
        if letter in vowels:
            list.append(counter)
    return list
