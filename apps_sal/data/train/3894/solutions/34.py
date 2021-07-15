solve = lambda s:getattr(s,["lower","upper"][sum(map(str.isupper, s))>len(s)//2])()
