def baubles_on_tree(baubles, branches):
    if not branches: return "Grandma, we will have to buy a Christmas tree first!"
    d,r=divmod(baubles,branches)
    return [d+1]*r+[d]*(branches-r)
