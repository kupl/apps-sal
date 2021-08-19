def reverse_words(text):
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    if '  ' in text:
        return '  '.join(words)
    return ' '.join(words)
