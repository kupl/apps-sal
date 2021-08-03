from re import findall as f
def bracket_buster(s): return f(r"\[(.*?)\]", s) if isinstance(s, str) else "Take a seat on the bench."
