def get_ic(msg):
    frequency = {}
    ic = 0.0
    for c in msg:
        if c in msg.lower():
            frequency[c] = msg.count(c, 0, len(msg))
    # print(frequency)
    return sum(map(lambda x: x * (x - 1), frequency.values())) / (len(msg) * (len(msg) - 1))


def get_key_length(cipher_text, max_key_length):
    ics = [0.0] * max_key_length
    for i, ic in enumerate(ics):
        if i > 1:
            sum_ic = 0.0
            avg_ic = 0.0
            offset = 0
            for x in range(i):
                offset = x
                step = i
                sum_ic += get_ic(cipher_text[offset::step])
            avg_ic = sum_ic / i
            ics[i] = avg_ic
    # for ic in ics:
    #    print(ic)
    return ics.index(max(ics))
