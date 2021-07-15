from re import findall as f
bracket_buster=lambda s:f(r"\[(.*?)\]",s) if isinstance(s,str) else "Take a seat on the bench."
