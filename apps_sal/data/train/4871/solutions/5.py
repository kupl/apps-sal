def letter_frequency(text):
  text = text.lower()
  freq_count = [(c, text.count(c)) for c in text if c.isalpha()]
  return sorted(list(set(freq_count)), key=lambda x: (-x[1], x[0]))


