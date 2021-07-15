def combo(*letters):
    if set(letters) == {'*'} : return 'X'
    if set(letters) == {'.'} : return '.'
    return '*'
    

def combs(*combs):
    print(combs)
    combos = []
    combs = sorted(combs, key=len)
    combs = [combs[0]+'.'*len(combs[1]), '.'*len(combs[0])+combs[1]]
    for _ in range(len(combs[1])):
        combos.append(''.join(combo(a,b) for a,b in zip(*combs)).strip('.'))
        combs[0] = '.' + combs[0]
        combs[1] = combs[1] + '.'
            
    return min(len(c) for c in combos if 'X' not in c)
    
    
    
        
        
        

