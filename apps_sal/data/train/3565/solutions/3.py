from collections import Counter

def solve(letters, removes):
  letter_counts = Counter(letters)
  unique_sorted_letters = sorted(letter_counts.keys())

  for letter in unique_sorted_letters:
    amount_to_remove = letter_counts[letter] if removes >= letter_counts[letter] else removes
    letters = letters.replace(letter, '', amount_to_remove)
    removes -= amount_to_remove

  return letters
