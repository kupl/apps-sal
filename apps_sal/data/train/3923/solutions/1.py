def micro_world(bact, k):
    bact = sorted(bact)
    return sum((1 for (i, a) in enumerate(bact) if all((a == b or a + k < b for b in bact[i + 1:]))))
