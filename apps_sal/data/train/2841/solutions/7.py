points = []
for x in range(1, 200): 
    points.extend([x]*4)
points = points[::-1]

def char_attribute(score):
    print(score)
    mod = (-5 + score//2) if score else score
    max_spell = -1 if score < 10 else 0 if score==10 else 9
    extra = points[-mod:][:9] if mod > 0 else []
    return {"modifier": mod, "maximum_spell_level": max_spell, "extra_spells": extra}
