calculate_tip=lambda a,r,R="terrible poor good great excellent".split():int(
R.index(r.lower())*a*.05+1-1e-9)if r.lower()in R else"Rating not recognised"
