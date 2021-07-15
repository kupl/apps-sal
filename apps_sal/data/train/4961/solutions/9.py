box=lambda A:(lambda X,Y:{"nw":[max(X),min(Y)],"se":[min(X),max(Y)]})(*zip(*A))
