encode=lambda m,k: (lambda k: [ord(l)-96+int(k[i%len(k)]) for i,l in enumerate(m)])(str(k))
