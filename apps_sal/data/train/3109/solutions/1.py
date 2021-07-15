sort_word=lambda w,l:(lambda a:''.join(next(a)if c.isalpha()else c for c in w))(iter(l[:len(l)>1]+sorted(l[1:-1])+l[-1:]))
scramble_words=lambda s:' '.join(sort_word(w,list(filter(str.isalpha,w)))for w in s.split())
