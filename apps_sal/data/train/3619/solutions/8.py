is_dd=lambda n:any(int(c)==x for c,x in __import__("collections").Counter(str(n)).items())
