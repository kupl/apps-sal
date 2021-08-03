def replace_exclamation(s):

    return s.translate(s.maketrans('aeiuoAIUEO', '!' * 10))
