to_bytes=b=lambda n,f=1:n and b(n>>8,0)+[format(n&255,'08b')]or['0'*8]*f
