def lemming_battle(N, G, B):
    while G and B:
        G.sort()
        B.sort()
        current = []
        for i in range(min(N, len(G), len(B))):
            current.append(G.pop() - B.pop())
        while current:
            x = current.pop()
            if x:
                (G if x > 0 else B).append(abs(x))
    if (not (G or B)):
        return "Green and Blue died"
    return "{} wins: {}".format("Green" if G else "Blue", " ".join(str(x) for x in sorted(G + B, reverse=True)))
