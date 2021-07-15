def commas(s):
    s = round(s,3)
    return format([int(s),s][s!=int(s)],',')
