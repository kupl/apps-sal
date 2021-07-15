S=lambda h,t={ord(s):' '+s for s in 'SDHC'}:h.translate(t).split()
sort_poker=lambda a,b:(lambda s,r:''.join(sorted(S(a),key=lambda c:(s[c[0]],r[c[1]])))
)(*[{c[0]:i for i,c in enumerate(S(p))}for p in(b,"2 3 4 5 6 7 8 9 10 J Q K A")])
