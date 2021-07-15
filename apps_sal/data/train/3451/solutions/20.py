triangle=t=lambda r:len(r)>1and t(''.join(a if a==b else(set('RGB')-{a,b}).pop()for a,b in zip(r,r[1:])))or r
