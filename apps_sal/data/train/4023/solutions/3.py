def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))
