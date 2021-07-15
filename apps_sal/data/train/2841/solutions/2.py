def char_attribute(score):
    modifier = score and (score - 10) // 2
    extra_spells = [i//4 for i in reversed(range(score//2-10, score//2-1)) if i > 3]
    maximum_spell_level = min(score-10, 9) if score >= 10 else -1
    return {
        'modifier': modifier,
        'maximum_spell_level': maximum_spell_level,
        'extra_spells': extra_spells,
    }
