t=dict(zip('.tlcgsaeiou','shell tomato lettuce cheese guacamole salsa'.split()+['beef']*5))
tacofy=lambda s:[t[c]for c in'.%s.'%s.lower()if c in t]
