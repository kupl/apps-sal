def de_nico(key, msg):

    decoder = []

    # assign key letters numbers according to alphabetized/sorted indices
    for letter in key:
        decoder.append(sorted(key).index(letter))

    # break msg into segments based on key length
    msg_segs = [msg[i:(i + len(key))] for i in range(0, len(msg), len(key))]

    # enumerate segments along their ranges
    enum_segs = []
    for seg in msg_segs:
        enum_segs.append(dict(zip(range(len(seg)), seg)))

    # read segs back into decoded_msg by codon in decoder, excepting KeyErrors out to account for final
    # seg length < len(decoder)
    decoded_msg = []
    for seg in enum_segs:
        for codon in decoder:
            try:
                decoded_msg.append(seg[codon])
            except KeyError:
                continue

    return ((''.join(decoded_msg)).rstrip())
