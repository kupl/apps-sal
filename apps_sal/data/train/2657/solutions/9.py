def make_string(s):
    return ''.join([s.split()[i][0] for i in range(len(s.split()))])
