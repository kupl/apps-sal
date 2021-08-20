def vowel_indices(word):
    vowels = 'aeiouyAEIOUY'
    count = 0
    vowel_list = []
    for x in word:
        count += 1
        if x in vowels:
            vowel_list.append(count)
    return vowel_list
