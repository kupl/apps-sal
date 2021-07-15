solve=lambda s,s1:any(s.count(i)>=2 and i not in s1 for i in s) or 2
