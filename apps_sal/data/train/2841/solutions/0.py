def char_attribute(score):
    return {'modifier': 0, 'maximum_spell_level': -1, 'extra_spells': []} if not score else {'modifier': score // 2 - 5, 'maximum_spell_level': -1 if score // 2 - 5 < 0 else min(9, score - 10), 'extra_spells': [1 + n // 4 for n in range(score // 2 - 5)][::-1][:9]}
