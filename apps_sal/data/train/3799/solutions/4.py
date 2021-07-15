def baubles_on_tree(baubles, branches):
    if not branches:
        return "Grandma, we will have to buy a Christmas tree first!"
    extra = baubles - (baubles//branches) * branches
    l = []
    for i in range(branches):
        l.append((baubles//branches)+1*(extra > 0))
        extra -= 1
    return l
