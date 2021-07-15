def freq_seq(s, sep):
    return sep.join([str(s.count(letter)) for letter in s])
