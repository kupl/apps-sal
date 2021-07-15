def bird_code(arr):
    codes = []
    
    for name in arr:
        name = name.replace("-", " ").split()
        
        if len(name) == 1:
            code = name[0][:4]
        
        elif len(name) == 2:
            code = name[0][:2] + name[1][:2]
        
        elif len(name) == 3:
            code = name[0][0] + name[1][0] + name[2][:2]
        
        elif len(name) == 4:
            code = "".join(n[0] for n in name)
        
        else:
            return "More than 4 words!"
        
        codes.append(code.upper())
    
    return codes
