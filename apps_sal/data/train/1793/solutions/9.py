class PlayingCards:
    codex = tuple(n+suit for suit in 'CDHS' for n in 'A23456789TJQK')
    ix = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    xi = {ch:i for i,ch in enumerate(ix)}
    
    @staticmethod
    def encode(s):
        q = 0
        tiers = PlayingCards.get_tiers()
        for ch in s:
            if ch not in PlayingCards.xi: return
            q *= 27
            q += PlayingCards.xi[ch]
        if q >= 52*tiers[0]: return
        for i,x in enumerate(tiers):
            if q >= x: break
        codex = list(PlayingCards.codex[:i])
        cdx = list(PlayingCards.codex[i:])
        for n in tiers[i:]:
            v = q // n
            q %= n
            codex.append(cdx.pop(v))
        return codex + cdx
    
    @staticmethod
    def decode(r):
        if set(r) != set(PlayingCards.codex): return
        q = 0
        tiers = PlayingCards.get_tiers()
        for i,card in enumerate(r):
            if card != PlayingCards.codex[i]: break
        tiers = tiers[i:]
        cdx = list(PlayingCards.codex[i:])
        for card,tier in zip(r[i:],tiers):
            j = cdx.index(card)
            q += j * tier
            cdx.pop(j)
        s = ''
        while q:
            v = q % 27
            q //= 27
            s += PlayingCards.ix[v]
        return s[::-1]
    
    @staticmethod
    def get_tiers():
        r = []
        c = 1
        for i in range(1,52):
            c *= i
            r.append(c)
        return r[::-1]
