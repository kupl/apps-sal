def encode(msg, k):
    return [ord(m)-96+int(str(k)[i%len(str(k))]) for i,m in enumerate(msg)]
