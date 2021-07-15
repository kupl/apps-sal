inseq, seq = {0}, [0]
for n in range(1, 10 ** 6):
    x = seq[-1] - n
    if x < 0 or x in inseq: x += 2*n
    seq.append(x)
    inseq.add(x)

recaman = seq.__getitem__
