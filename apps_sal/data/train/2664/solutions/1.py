solve=lambda s:any(s[:y]+c+s[y+1:]==(s[:y]+c+s[y+1:])[::-1]!=s for y,x in enumerate(s)for c in set(s))
