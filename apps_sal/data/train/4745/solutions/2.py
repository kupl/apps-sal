def group_groceries(groceries):
    groceries = groceries.split(',')
    carne = []
    fruta = []
    outro = []
    vegetal = []
    for item in groceries:
        a = item.split('_')
        if a[0] == 'fruit':
            fruta.append(a[1])
        elif a[0] == 'meat':
            carne.append(a[1])
        elif a[0] == 'vegetable':
            vegetal.append(a[1])
        else:
            outro.append(a[1])
    b = 'fruit:{}\nmeat:{}\nother:{}\nvegetable:{}'.format(','.join(sorted(fruta)), ','.join(sorted(carne)), ','.join(sorted(outro)), ','.join(sorted(vegetal)))
    return b
