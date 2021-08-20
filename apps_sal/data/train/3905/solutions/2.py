def missing(seq):
    digits = 1
    while digits <= len(seq) // 2:
        my_seq = last = seq[:digits]
        n = int(my_seq)
        missing = None
        while len(my_seq) < len(seq):
            n += 1
            my_seq += str(n)
            if not seq.startswith(my_seq):
                if missing == None:
                    missing = n
                    my_seq = last
                else:
                    break
            else:
                last = my_seq
        if my_seq == seq and missing:
            return missing
        digits += 1
    return -1
