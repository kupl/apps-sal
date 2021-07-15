def char_attribute(score):
    
    result = {}
    
    #modifier
    result["modifier"] = 0 if score == 0 else score //2 - 5
    
    #maximum_spell_level
    result["maximum_spell_level"] = -1 if score < 10 else min(9, score -10)
    
    #extra_spells         
    result["extra_spells"] = [1 + n//4 for n in range(result["modifier"])][::-1][:9]
    
    return result
