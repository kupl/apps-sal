def revamp(s):
    words = ["".join(sorted(word)) for word in s.split()]
    return " ".join(sorted(words, key=lambda word: (sum(ord(c) for c in word), len(word), word)))
