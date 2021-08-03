def reverse_and_combine_text(text):
    words = text.split()
    while len(words) > 1:
        words = [''.join(w[::-1] for w in words[i:i + 2]) for i in range(0, len(words), 2)]
    return ''.join(words)
