def baubles_on_tree(baubles, branches):
    return "Grandma, we will have to buy a Christmas tree first!" if not branches else [ baubles//branches + (1 if i<baubles%branches else 0) for i in range(branches) ]
