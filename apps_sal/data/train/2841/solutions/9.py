def char_attribute(score):
    attributes = {"modifier": 0, "maximum_spell_level": -1, "extra_spells": []}
    if score == 0:
        return attributes
    modifier = score // 2 - 5
    attributes['modifier'] = modifier
    if modifier < 0:
        return attributes
    else:
        attributes['maximum_spell_level'] = min(9, score-10)
        extra_spells = []
        for i in range(min(9, modifier)):
            extra = (modifier - 1 - i) // 4
            extra_spells.append(1 + extra)
        attributes['extra_spells'].extend(extra_spells)
        return attributes
