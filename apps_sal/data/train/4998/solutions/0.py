def wanted_words(vowels, consonants, forbidden):
    return [w for w in WORD_LIST if len(w) == vowels + consonants and sum(map(w.count, 'aeiou')) == vowels and (not any((c in w for c in forbidden)))]
