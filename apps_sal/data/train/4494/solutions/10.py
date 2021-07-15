points = lambda g: sum((x==y)+(x>y)*3 for x,_,y in g)
