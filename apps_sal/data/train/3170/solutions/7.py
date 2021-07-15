# Why not both? :)

def longer(s):
    return " ".join(sorted(list(s.split()), key=lambda x: (len(x), x)))
    
longer = lambda s: " ".join(sorted(list(s.split()), key=lambda x: (len(x), x)))    
