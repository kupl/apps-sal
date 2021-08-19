from operator import itemgetter


def de_nico(key, msg):
    (decryptkey, _) = zip(*sorted(zip(range(1, len(key) + 1), key), key=itemgetter(1)))
    decryptkey = ''.join((str(x) for x in decryptkey))
    chunksize = len(decryptkey)
    chunks = [msg[y - chunksize:y] for y in range(chunksize, len(msg) + chunksize, chunksize)]
    for (i, chunk) in enumerate(chunks):
        (chunkSorted, _) = zip(*sorted(zip(chunk, decryptkey), key=itemgetter(1)))
        chunks[i] = ''.join(chunkSorted)
    return ''.join(chunks).rstrip()
