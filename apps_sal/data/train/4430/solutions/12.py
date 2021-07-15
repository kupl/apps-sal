vowel_2_index=lambda s: ''.join([str(i+1) if x.lower() in "aeiou" else x for i,x in enumerate(s)])

