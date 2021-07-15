from re import finditer
def case_unification(word):
    return word.lower() if len(list(finditer(r'([a-z])', word))) > len(list(finditer(r'([A-Z])', word))) else word.upper()

