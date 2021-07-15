def mutations(alice, bob, word, first):
    
    def isValid(w): return w not in seen and sum(a==b for a,b in zip(w,word))==3 and len(set(w))==4
    
    players, seen  = [alice,bob], {word}
    win, failed, i = -1, -1, first^1
    while 1:
        i    ^= 1
        lst   = players[i]
        found = next((w for w in lst if isValid(w)), None)
        if found is None:
            if failed==i^1: break
            failed = i
        else:
            seen.add(found)
            word, win = found, i
            if failed!=-1: break
    return win
