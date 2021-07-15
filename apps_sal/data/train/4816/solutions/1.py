def child(bird1, bird2):
    return 1 <= sum(i != j for i, j in zip(bird1, bird2)) <= 2 

def grandchild(bird1, bird2):
    return bird1 == bird2 or sum(i != j for i, j in zip(bird1, bird2)) <= 4 and len(bird1) > 1

