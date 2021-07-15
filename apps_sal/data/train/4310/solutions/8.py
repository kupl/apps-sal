def swap(stg):
    return "".join(char.upper() if char in "aeiou" else char for char in stg)
