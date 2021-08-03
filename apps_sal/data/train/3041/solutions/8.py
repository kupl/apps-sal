def vowel_start(s): return ''.join(' ' * (x in 'aeiou') + x * x.isalnum()for x in s.lower()).strip()
