def hydrate(s): 
    a = sum(map(int, filter(str.isdigit, s)))
    return f"{a} glass{['es', ''][a == 1]} of water"
