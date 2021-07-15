def find_missing_number(seq):
    try:seq=sorted(map(int,seq.split()))
    except ValueError:return 1
    if not seq:return 0
    if seq[0]!=1:return 1
    for i,v in enumerate(seq[:-1]):
        if v+1!=seq[i+1]:
            return v+1
    return 0
