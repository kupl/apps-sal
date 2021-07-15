def alphabetized(stg):
    return "".join(sorted((c for c in stg if c.isalpha()), key=str.lower))
