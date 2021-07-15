decode=lambda c,k:''.join(chr(a-int(b)+96)for a,b in zip(c,str(k)*30))
