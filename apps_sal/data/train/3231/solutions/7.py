from re import finditer


def case_unification(word):
    return word.lower() if len(list(finditer('([a-z])', word))) > len(list(finditer('([A-Z])', word))) else word.upper()
