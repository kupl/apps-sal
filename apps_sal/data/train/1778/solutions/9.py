def get_key_length(cipher_text, max_key_length):
    IC = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(2, max_key_length + 1):
        avg_ic = 0
        for j in range(i):
            ic = 0
            txt = cipher_text[j::i]
            l = len(txt)
            for k in alphabet:
                c = txt.count(k)
                n = c * (c - 1) / (l * (l - 1))
                ic += n
            avg_ic += ic
        avg_ic /= i
        IC.append(avg_ic)
    return IC.index(max(IC)) + 2
