def letter_frequency(text):
    text = [c for c in text.lower() if c.isalpha()]
    result = [(char, text.count(char)) for char in sorted(set(text))]
    return sorted(result, key=lambda char_freq: char_freq[1], reverse=True)
