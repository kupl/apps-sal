def vowel_2_index(s): return ''.join(str(i)if e in 'aiueoAIUEO' else e for i, e in enumerate(s, 1))
