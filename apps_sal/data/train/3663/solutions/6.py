four_piles=lambda n,y: (lambda r: r if all(e%1==0 and e>0 for e in r) else [])((lambda x: [x+y,x-y,x*y,x/y])(n*y/(2*y+y*y+1)))
