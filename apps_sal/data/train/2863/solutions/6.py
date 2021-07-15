def alan_annoying_kid(stg):
    response = "I don't think you {0} today, I think you {1} {2} {3}!".format
    what = stg.replace("Today I ", "")[:-1]
    made = what.replace("didn't ", "").split()[0]
    filler = (what, "did", made, "it") if "didn't" in what else (what, "didn't", made[:-2], "at all")
    return response(*filler)

