def de_nico(key, msg):
    num_key = ''.join([str(id) for i in key for id, item in enumerate(sorted(key), 1) if item == i])
    cut_msg = [msg[i:i + len(num_key)] for i in range(0, len(msg), len(num_key))]
    d_msg = [''.join([item for i in num_key for id, item in enumerate(list(x), 1) if id == int(i)]) for x in cut_msg]
    return ''.join(d_msg).rstrip()
