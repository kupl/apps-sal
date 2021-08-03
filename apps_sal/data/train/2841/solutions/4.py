def char_attribute(score):
    modifier = (score - 10) // 2 if score > 0 else 0
    m_spell = min(max(-1, score - 10), 9)
    e_spells = []
    x = 0
    for i in range((score - 10) // 2):
        if i % 4 == 0:
            x += 1
        e_spells.insert(0, x)
    return {'modifier': modifier, 'maximum_spell_level': m_spell, 'extra_spells': e_spells[:9]}
