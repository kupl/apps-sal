def sat(f: Formula):
    literals = total_literals(f, {})
    length = len(literals)

    for b in range(2**length):
        table = {i:int(j) for i,j in zip(list(literals.keys()), bin(b)[2:].zfill(length))}
        if satisfiable(f, table):
            return {literals[i] for i in table if table[i]}
    return False
    
def total_literals(f, lit):
    for i in f.args:
        if i.is_literal() : lit[i.name] = i
        else : total_literals(i, lit)
    return lit 

def satisfiable(f, table):
    if f.is_literal() : return table[f.name]
    x = [satisfiable(i,table) for i in f.args]    
    return all(x) if f.is_and() else any(x) if f.is_or() else not all(x)

#very INeffecient

