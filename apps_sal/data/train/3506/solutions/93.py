def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x in 'AEIOUYaeiouy']
