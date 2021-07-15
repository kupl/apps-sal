d = {j:i for i,j in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
base64_to_base10=lambda s:sum(d[j]*(64**(len(s)-1-i)) for i,j in enumerate(s))
