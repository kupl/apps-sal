spin_words = lambda s: ' '.join([
len(w) > 4 and w[::-1] or w
for w in s.split()
])
