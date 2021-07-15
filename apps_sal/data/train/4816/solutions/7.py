from operator import ne

def child(bird1, bird2):
    return 1 <= sum(map(ne, bird1, bird2)) <= 2

def grandchild(bird1, bird2):
    return sum(map(ne, bird1, bird2)) <= 4 and bird1 + bird2 not in 'BWB'
