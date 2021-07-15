sort_grades=lambda l:sorted(l,key=lambda g:float(g[1:].replace('+','.5').replace('B','-1')))
