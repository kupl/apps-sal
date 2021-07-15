def sort_string(stg):
    stg_ascii = (char for char in stg if char.isalpha())
    sorted_ascii = iter(sorted(stg_ascii, key=str.lower))
    return "".join(next(sorted_ascii) if char.isalpha() else char for char in stg)
