def order(pizzas, salads, appetizers):
    if pizzas <= 10:
        pizzas= 10 + 1.5 * pizzas
    elif pizzas <=20:
        pizzas = 20 + 1.5 * pizzas
    if pizzas > salads*3 + appetizers*5: 
        return pizzas
    else: 
        return salads*3 + appetizers*5
    

