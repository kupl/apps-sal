def animals(heads, legs):
    cow = (legs - 2 * heads) / 2
    if cow < 0 or cow != round(cow):
        return "No solutions"
    chicken = heads - cow
    if chicken < 0:
        return "No solutions"
    return (chicken, cow)
