split_exp=lambda n: (lambda d: [e+ "0"*(d-i-1) if d>i else "."+"0"*(i-d-1)+e for i,e in enumerate(n) if e not in ".0"])(n.index(".") if "." in n else len(n))
