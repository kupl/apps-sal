def inside_out(s):
    return ' '.join(w[:len(w)//2][::-1] + w[len(w)//2:(len(w)+1)//2] + w[(len(w)+1)//2:][::-1] for w in s.split())
