def char_attribute(score):
    if score > 0:
        mod = score//2 - 5
    else:
        mod = 0
    
    if score > 11:
        bonus_spells = [max(0,(score - i)//8) for i in range(4,21,2)]
        while min(bonus_spells) == 0:
            bonus_spells.pop()
    else:
        bonus_spells= []
    
    max_spell = min(9, max(-1,score-10))
    
    
    return {"modifier": mod, "maximum_spell_level": max_spell, "extra_spells":bonus_spells} 
