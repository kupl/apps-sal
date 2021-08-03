def baubles_on_tree(baubles, branches):
    return [baubles // branches + (i < baubles % branches) for i in range(branches)] if branches else 'Grandma, we will have to buy a Christmas tree first!'
