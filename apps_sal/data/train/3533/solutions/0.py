def de_nico(key, msg):
    ll, order, s = len(key), [sorted(key).index(c) for c in key], ''
    while msg:
        s, msg = s + ''.join(msg[i] for i in order if i < len(msg)), msg[ll:]
    return s.strip()
