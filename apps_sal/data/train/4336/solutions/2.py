def mem_alloc(banks):
    seen, turn = set(), 0
    
    while 1:
        saw = tuple(banks)
        if saw in seen: return turn
        seen.add(saw)
        
        im,m = max(enumerate(banks), key=lambda it: (it[1], -it[0]))
        n,r = divmod(m, len(banks))
        
        banks[im] = 0
        banks = [v+n for i,v in enumerate(banks)]
        for i in range(1,r+1): banks[(i+im) % len(banks)] += 1
        turn += 1
