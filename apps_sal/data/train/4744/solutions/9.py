def band_name_generator(s): return (['the ', s[:-1]][s[0] == s[-1]] + s).title()
