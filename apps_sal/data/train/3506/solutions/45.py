def vowel_indices(word):
    import re
    return [index + 1 for (index, element) in enumerate(word.lower()) if re.match('[aeiouy]', element)]
