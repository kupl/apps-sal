reverse_invert=lambda l: [(-1 if n>0 else 1)*int(str(abs(n))[::-1]) for n in l if type(n)==int]
