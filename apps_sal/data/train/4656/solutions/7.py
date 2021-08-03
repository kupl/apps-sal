def get_seq(string, slen):
    for i in range(1, slen + 1):
        sub = string[:i]
        times = slen // i
        if sub * times == string:
            return sub
    else:
        return False


def center_of(chars):
    if not chars:
        return chars
    seq = chars[0]
    chars_len = len(chars)

    i = 2
    lcount = 0
    while True:
        if i % 2:
            middle = chars[(lcount + (i // 2)) % chars_len]
            seq += middle
        else:
            lcount += 2 * i - 1
        i += 1
        lseq = len(seq)
        if lseq >= chars_len:
            subseq = get_seq(seq, lseq)
            if subseq:
                return subseq
