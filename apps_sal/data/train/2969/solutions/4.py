from itertools import starmap, product, count

def _complex_to_point(c):
    return int(c.real), int(c.imag)
    
def _neighbors(point):
    return (point + (1j ** i) for i in range(4))

def advice(agents, n):
    if not n:
        return []
    city = {complex(i, j): None for i, j in product(list(range(n)), repeat=2)}
    last = set(agent for agent in starmap(complex, agents) if agent in city)
    if not last:
        return sorted(_complex_to_point(cell) for cell in city)
    for dist in count():
        city.update({cell: dist for cell in last})
        next_cells = set(
            neighbor for cell in last for neighbor in _neighbors(cell) 
            if neighbor in city and city[neighbor] is None
        )
        if not next_cells:
            return [] if not dist else sorted(_complex_to_point(cell) for cell in last)
        last = next_cells
        
            
            

