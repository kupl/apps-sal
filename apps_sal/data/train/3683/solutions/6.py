def letter_count(s):
    return dict(((letter, s.count(letter)) for letter in sorted(set(s))))
