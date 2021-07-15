from operator import itemgetter
def de_nico(key,msg):
    #keyDict = dict(zip(sorted(key), range(1, len(key)+1)))
    #encryptkey = "".join([str(keyDict[x]) for x in key])
    decryptkey, _ = zip( *sorted(zip(range(1, len(key)+1), key), key = itemgetter(1) ))
    decryptkey = "".join(str(x) for x in decryptkey)
    chunksize = len(decryptkey)
    chunks = [msg[y-chunksize:y] for y in range(chunksize, len(msg)+chunksize, chunksize)]
    #chunks[-1] += " "*(len(key) - len(chunks[-1])) ## add whitespaces accordingly if the last chunk happens to be too short    
    for i, chunk in enumerate(chunks):
        chunkSorted, _ = zip( *sorted( zip(chunk, decryptkey), key = itemgetter(1) ))
        chunks[i] = "".join(chunkSorted)
    return "".join(chunks).rstrip()
