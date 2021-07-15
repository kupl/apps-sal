def wheres_wally(stg):
    i = stg.find("Wally")
    while i > -1 and (i and stg[i-1] != " " or stg[i+5:i+6].isalnum()):
        i = stg.find("Wally", i+1)
    return i
