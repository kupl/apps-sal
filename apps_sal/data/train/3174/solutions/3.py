import re
def derivative(s): return re.sub(r'\^1(?=[-+])', '', re.sub(r'\+-', '-', '+'.join([['', f'{int(i[0]if i[0]and i[0]not in"+-"else[1,-1][i[0]=="-"])*int(i[-1]or 1)}'][bool(i[-2])] + (f'x^{[0,int(i[-1])-1][bool(i[-2])]}'if i[-1]else'') for i in re.findall(r'([-+]?\d*)(x?)\^?(\d*)', s)]))).strip('+') or '0'
