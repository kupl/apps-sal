import re
how_many_bees=lambda b:0 if not b else sum([len(re.findall(r"bee", "".join(i+[' ']+i[::-1]))) for i in b]+[len(re.findall(r"bee", "".join(i+tuple(' ')+i[::-1]))) for i in zip(*b)])
