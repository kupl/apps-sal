solve=lambda s: s.upper() if len([l for l in s if ord(l)>64 and ord(l)<91])>len(s)//2 else s.lower()
