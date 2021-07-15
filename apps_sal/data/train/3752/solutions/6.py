value_at=lambda p, x: round(sum(map(lambda e: e[1]*c(x,e[0]), enumerate(p[::-1]))), 2)
c=lambda x,b: 1 if x==b or b<1 else x if b<2 else x*c(x-1,b-1)/b
