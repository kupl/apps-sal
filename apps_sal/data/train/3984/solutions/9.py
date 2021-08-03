t = dict(zip('.tlcgsaeiou', 'shell tomato lettuce cheese guacamole salsa'.split() + ['beef'] * 5))
def tacofy(s): return [t[c]for c in '.%s.' % s.lower()if c in t]
