def div_con(x): return sum(i for i in x if type(i) == int) - sum(int(s) for s in x if type(s) == str)
