def case_id(stg):
    print(stg)
    if "-" in stg and "_" not in stg and all(w.islower() for w in stg.split("-")):
        return "kebab"
    if "_" in stg and "-" not in stg and all(w.islower() for w in stg.split("_")):
        return "snake"
    if stg.isalpha() and any(c.isupper() for c in stg):
        return "camel"
    return "none"
