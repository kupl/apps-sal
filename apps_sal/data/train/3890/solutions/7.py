def get_honor_path(honor_score, target_honor_score):

    honor_needed = target_honor_score - honor_score
    kyus = {}
    
    if honor_score < target_honor_score and honor_needed != 0:
        
        kyus["1kyus"] = honor_needed // 2
        kyus["2kyus"] = honor_needed % 2
    
    return kyus
