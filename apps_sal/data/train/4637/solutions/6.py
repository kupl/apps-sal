from math import ceil
def convert_recipe(recipe):
    l = []
    l_recipe = recipe.split()
    for num, i in enumerate(l_recipe):
        if i == 'tbsp':
            tmp = l_recipe[num - 1]
            weight  = ceil(eval(tmp) * 15)  if '/' in tmp else int(tmp) * 15
            l.append('tbsp ({}g)'.format(weight))
        elif i == 'tsp':
            tmp = l_recipe[num - 1]
            weight  = ceil(eval(tmp) * 5)  if '/' in tmp else int(tmp) * 5
            l.append('tsp ({}g)'.format(weight))    
        else:
            l.append(i)   
    return ' '.join(l)        
            

