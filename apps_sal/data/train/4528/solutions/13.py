my_languages = lambda r: sorted({x:r[x] for x in r if r[x]>=60}, key=r.get, reverse=True)
