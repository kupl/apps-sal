from math import floor

def xp_to_target_lvl(*args):
    if len(args) != 2:
        return "Input is invalid."
    
    current_xp = args[0]
    target_lvl = args[1]
    if type(current_xp) is not int or type(target_lvl) is not int or current_xp < 0 or target_lvl <= 0 or target_lvl > 170:
        return "Input is invalid."
    
    req_xp = 0
    xp_lvl = 314
    for i in range(1,target_lvl):
        print(xp_lvl)
        req_xp += xp_lvl
        xp_lvl *= (1.25 - 0.01*((i+1)//10))
        xp_lvl = floor(xp_lvl)
    
    print(f"\n{req_xp}")
    
    return req_xp - current_xp if req_xp > current_xp else f"You have already reached level {target_lvl}."
