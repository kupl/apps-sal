def balanced_num(number):
    number = str(number)
    l1 = len(number)
    l2 = int((l1-0.5)//2)
    
    return ('Not Balanced', 'Balanced')[l1 < 3 or sum(map(int, number[:l2])) == sum(map(int, number[-l2:]))]
    

