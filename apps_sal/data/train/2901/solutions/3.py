inc = {1:2,2:6,3:11,4:17,5:25,6:35,7:46,8:58,9:72,10:88,11:106,12:126,13:147,14:170,15:195,16:221,17:250,18:280,19:311,20:343}

def psion_power_points(level,score):
    
    if level > 0 and score > 10:
        base_points = inc.get(level,343)        
    else:
        base_points = 0   
    
    bonus_points = max(0,int((score - 10) // 2 * 0.5 * level))
    
    return base_points + bonus_points #if score > 11 else base_points
