def seven_ate9(s): return ''.join(x for i, x in enumerate(s) if s[i - 1:i + 2] != "797")
