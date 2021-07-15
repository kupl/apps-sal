def coloque(bag,item,x,y):
    for i in range(len(item)) :
        for j in range(len(item[0])):
            if item[i][j] != 0 : bag[y+i][x+j] = item[i][j]
    return bag

def fit_recur(bag,items):
    print("\n",bag)
    item_h = len(items[0])
    item_w = len(items[0][0])
    
    for y in range(len(bag)):
        for x in range(len(bag[0])):
            if y + item_h <= len(bag) and x + item_w <= len(bag[0]):
                if sum([ (bag[y+i][x+j] == 0 or items[0][i][j] == 0) for i in range(item_h)  for j in range(item_w) ]) == item_h * item_w :
                    if len(items) > 1:
                        bag_r = []
                        for row in bag : bag_r.append(row[:])
                        bag_r = fit_recur(coloque(bag_r,items[0],x,y),items[1:])
                        if type(bag_r) == list: return bag_r
                    else: return coloque(bag,items[0],x,y)
    

def fit_bag(height: int, width: int, items: List[List[List[int]]]) -> List[List[int]]:
    bag = [[0 for i in range(width)] for j in range(height)]
    
    
    for item in items:  # First of all, if there is a null line at the border of the item, it is deleted
        while sum([ ite == 0 for ite in item[0] ]) == len(item[0])  : del item[0]
        while sum([ ite == 0 for ite in item[-1] ]) == len(item[-1])  : del item[-1]
      


    for i in range(1,len(items)):    #We sort the items to make the algorithm more eficient
        while i > 0 and  len(items[i]) >= len(items[i-1]) :
            aux = items[i]
            items[i] = items[i-1]
            items[i-1] = aux
            i = i-1
            
    print("\n Sorted items:", items , "\n")  
    
    return fit_recur(bag[:],items)  
