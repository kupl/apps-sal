from collections import Counter
validate_word=lambda word: len(set(Counter(word.lower()).values())) == 1
