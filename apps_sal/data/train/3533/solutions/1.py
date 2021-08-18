def de_nico(key, msg):

    decoder = []

    for letter in key:
        decoder.append(sorted(key).index(letter))

    msg_segs = [msg[i:(i + len(key))] for i in range(0, len(msg), len(key))]

    enum_segs = []
    for seg in msg_segs:
        enum_segs.append(dict(zip(range(len(seg)), seg)))

    decoded_msg = []
    for seg in enum_segs:
        for codon in decoder:
            try:
                decoded_msg.append(seg[codon])
            except KeyError:
                continue

    return ((''.join(decoded_msg)).rstrip())
